deps := $(patsubst %.cpp,%.o,$(wildcard *.cpp))

all: prebuild $(deps)

%.o: %.cpp
	clang++ -Ofast -std=c++20 -mllvm -polly -mllvm -polly-parallel -lgomp $< -o out/cpp/$(basename $<)
	cp $(basename $<).py out/py/

clean:
	rm -rf out

setup:
	-mkdir out
	-mkdir out/cpp
	-mkdir out/py

prebuild: clean setup
