.PHONY: paper exact-mean clean

paper:
	mkdir -p build
	pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build paper/main.tex
	pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build paper/main.tex

exact-mean:
	mkdir -p build
	$(CXX) -O3 -std=c++20 -Wall -Wextra -Wpedantic -fopenmp code/exact_mean.cpp -o build/exact_mean

clean:
	rm -f build/main.aux build/main.log build/main.out build/main.pdf build/exact_mean
