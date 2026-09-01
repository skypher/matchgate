#include <algorithm>
#include <cerrno>
#include <cmath>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>

#include <omp.h>

namespace {

void print_usage(std::ostream& output, const char* program_name) {
  output << "Usage: " << program_name << " [--rho DENSITY] [N ...]\n"
         << "Numerically evaluate the exact finite-sum mean distance for "
            "matchgate components.\n\n"
         << "Arguments:\n"
         << "  N              Positive matchgate site counts (default: "
            "25 50 100 200 400 800).\n\n"
         << "Options:\n"
         << "  --rho DENSITY  Requested subset density in (0,1) (default: 0.5).\n"
         << "  -h, --help     Show this help message and exit.\n";
}

long double log_choose(int n, int k) {
  if (k < 0 || k > n) {
    return -std::numeric_limits<long double>::infinity();
  }
  return std::lgammal(static_cast<long double>(n) + 1.0L)
       - std::lgammal(static_cast<long double>(k) + 1.0L)
       - std::lgammal(static_cast<long double>(n - k) + 1.0L);
}

// If H and H' are independent Hypergeometric(N, k, r) variables, return
// E|H-H'|.  The probability vector is normalized after subtracting its
// largest logarithm, which keeps the computation stable for large N.
long double expected_abs_hypergeom_difference(int N, int k, int r) {
  const int lo = std::max(0, k - (N - r));
  const int hi = std::min(k, r);
  std::vector<long double> log_weights;
  log_weights.reserve(static_cast<std::size_t>(hi - lo + 1));

  long double max_log_weight = -std::numeric_limits<long double>::infinity();
  for (int j = lo; j <= hi; ++j) {
    const long double value = log_choose(r, j) + log_choose(N - r, k - j);
    log_weights.push_back(value);
    max_log_weight = std::max(max_log_weight, value);
  }

  std::vector<long double> probabilities(log_weights.size());
  long double normalization = 0.0L;
  for (std::size_t index = 0; index < log_weights.size(); ++index) {
    probabilities[index] = std::exp(log_weights[index] - max_log_weight);
    normalization += probabilities[index];
  }
  for (long double& probability : probabilities) {
    probability /= normalization;
  }

  // 2 sum_j p_j sum_{h<j} p_h (j-h), evaluated from prefix mass and
  // prefix first moment.
  long double prefix_mass = 0.0L;
  long double prefix_moment = 0.0L;
  long double expectation = 0.0L;
  for (int j = lo; j <= hi; ++j) {
    const long double probability = probabilities[static_cast<std::size_t>(j - lo)];
    expectation += 2.0L * probability
                 * (static_cast<long double>(j) * prefix_mass - prefix_moment);
    prefix_mass += probability;
    prefix_moment += static_cast<long double>(j) * probability;
  }
  return expectation;
}

long double exact_expected_distance(int n, int k) {
  const int N = 2 * n;
  long double total = 0.0L;
#pragma omp parallel for schedule(dynamic, 8) reduction(+ : total)
  for (int r = 1; r < N; ++r) {
    total += expected_abs_hypergeom_difference(N, k, r);
  }
  return total;
}

long double central_symmetric_difference_expectation(int n) {
  const long double log_denominator = log_choose(2 * n, n);
  long double total = 0.0L;
  for (int m = 1; m <= n; ++m) {
    const long double probability =
        std::exp(2.0L * log_choose(n, m) - log_denominator);
    const long double bridge_area =
        0.5L * static_cast<long double>(m)
        * std::exp(static_cast<long double>(m) * std::log(4.0L)
                   - log_choose(2 * m, m));
    const long double stretch =
        static_cast<long double>(2 * n + 1) / static_cast<long double>(2 * m + 1);
    total += probability * stretch * bridge_area;
  }
  return total;
}

int parse_positive_integer(const std::string& text) {
  errno = 0;
  char* end = nullptr;
  const long value = std::strtol(text.c_str(), &end, 10);
  if (errno != 0 || end == text.c_str() || *end != '\0' || value <= 0
      || value > std::numeric_limits<int>::max() / 2) {
    throw std::invalid_argument("invalid positive integer: " + text);
  }
  return static_cast<int>(value);
}

long double parse_density(const std::string& text) {
  errno = 0;
  char* end = nullptr;
  const long double value = std::strtold(text.c_str(), &end);
  if (errno != 0 || end == text.c_str() || *end != '\0'
      || !(value > 0.0L && value < 1.0L)) {
    throw std::invalid_argument("density must lie strictly between 0 and 1: " + text);
  }
  return value;
}

}  // namespace

int main(int argc, char** argv) {
  try {
    for (int index = 1; index < argc; ++index) {
      const std::string argument(argv[index]);
      if (argument == "-h" || argument == "--help") {
        print_usage(std::cout, argv[0]);
        return 0;
      }
    }

    long double requested_density = 0.5L;
    std::vector<int> site_counts;
    for (int index = 1; index < argc; ++index) {
      const std::string argument(argv[index]);
      if (argument == "--rho") {
        if (index + 1 >= argc) {
          throw std::invalid_argument("--rho requires a value");
        }
        requested_density = parse_density(argv[++index]);
      } else {
        site_counts.push_back(parse_positive_integer(argument));
      }
    }
    if (site_counts.empty()) {
      site_counts = {25, 50, 100, 200, 400, 800};
    }

    std::cout << std::setprecision(std::numeric_limits<long double>::max_digits10);
    std::cout << "threads=" << omp_get_max_threads()
              << " requested_density=" << requested_density
              << '\n';

    const long double pi = std::acos(-1.0L);
    for (std::size_t case_index = 0; case_index < site_counts.size(); ++case_index) {
      const int n = site_counts[case_index];
      const int N = 2 * n;
      int k = static_cast<int>(std::llround(requested_density * N));
      k = std::clamp(k, 1, N - 1);
      const long double rho = static_cast<long double>(k) / N;
      const long double predicted_constant =
          std::sqrt(2.0L * pi) * std::sqrt(rho * (1.0L - rho)) / 2.0L;

      std::cout << "case " << (case_index + 1) << '/' << site_counts.size()
                << " n=" << n << " k=" << k << " phase=exact_sum" << '\n';
      std::cout.flush();

      const double started = omp_get_wtime();
      const long double expectation = exact_expected_distance(n, k);
      const double elapsed = omp_get_wtime() - started;
      const long double n_to_three_halves =
          static_cast<long double>(n) * std::sqrt(static_cast<long double>(n));
      const long double normalized = expectation / n_to_three_halves;
      const long double correction_over_n =
          (expectation - predicted_constant * n_to_three_halves) / n;

      long double mixture_expectation = std::numeric_limits<long double>::quiet_NaN();
      long double mixture_difference = std::numeric_limits<long double>::quiet_NaN();
      long double observed_sqrt_correction =
          std::numeric_limits<long double>::quiet_NaN();
      long double two_term_residual_times_sqrt_n =
          std::numeric_limits<long double>::quiet_NaN();
      if (k == n) {
        mixture_expectation = central_symmetric_difference_expectation(n);
        mixture_difference = mixture_expectation - expectation;
        const long double predicted_sqrt_correction =
            -5.0L * predicted_constant / 16.0L;
        const long double sqrt_n = std::sqrt(static_cast<long double>(n));
        observed_sqrt_correction =
            (expectation - predicted_constant * n_to_three_halves) / sqrt_n;
        two_term_residual_times_sqrt_n =
            (expectation - predicted_constant * n_to_three_halves
             - predicted_sqrt_correction * sqrt_n) * sqrt_n;
      }

      std::cout << "result n=" << n
                << " k=" << k
                << " rho=" << rho
                << " expectation=" << expectation
                << " normalized=" << normalized
                << " limit_constant=" << predicted_constant
                << " correction_over_n=" << correction_over_n
                << " mixture_expectation=" << mixture_expectation
                << " mixture_difference=" << mixture_difference
                << " observed_sqrt_correction=" << observed_sqrt_correction
                << " two_term_residual_times_sqrt_n="
                << two_term_residual_times_sqrt_n
                << " elapsed_seconds=" << elapsed << '\n';
      std::cout.flush();
    }
    return 0;
  } catch (const std::exception& exception) {
    std::cerr << "error: " << exception.what() << '\n';
    return 1;
  }
}
