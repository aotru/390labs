PYTHON ?= python3 # Python 3 executable
CXX ?= g++ # C++ compiler
CXXFLAGS ?= --std=c++17 -g

test: list_parser.doctest bv

bv: BitVector_test.exe BitVector.testrun

%.doctest:
	$(PYTHON) -m doctest $(@:.doctest=.py)

BitVector_test.exe: BitVector.hpp BitVector_test.cpp
	$(CXX) $(CXXFLAGS) $(@:.exe=.cpp) -o $@

%.testrun:
	./$(@:.testrun=_test.exe) > $(@:.testrun=_test.out)
	diff -q $(@:.testrun=_test.out) $(@:.testrun=_test.correct)

clean:
	rm -rf *.out __pycache__ *.exe *.exe.dSYM
