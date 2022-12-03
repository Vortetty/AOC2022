deps := $(patsubst %.cpp,%.o,$(wildcard *.cpp)) $(wildcard *.py)
flags := -Ofast -std=c++20 -s

all: prebuild $(deps)
all-polly: prebuild pollysetup $(deps)

%.o: %.cpp
	clang++ $(flags) $< -o out/cpp/$(basename $<)

%.py: %.py
	cp $(basename $<).py out/py/

clean:
	rm -rf out

setup:
	-mkdir out
	-mkdir out/cpp
	-mkdir out/py

prebuild: clean setup

pollysetup:
	$(eval flags := $(flags) -mllvm -polly -mllvm -polly-parallel -lgomp)
