deps := $(patsubst %.cpp,out/cpp/%,$(wildcard *.cpp)) $(patsubst %.py,out/py/%.py,$(wildcard *.py))
flags := -Ofast -std=c++20 -s

all: prebuild $(deps)
all-polly: prebuild pollysetup $(deps)

out/cpp/%: %.cpp
	clang++ $(flags) $< -o out/cpp/$(basename $<)

out/py/%.py: %.py
	cp $(basename $<).py out/py/

clean:
	rm -rf out

setup:
	@mkdir -p out
	@mkdir -p out/cpp
	@mkdir -p out/py

prebuild: setup

pollysetup:
	$(eval flags := $(flags) -mllvm -polly -mllvm -polly-parallel -lgomp)
