PYTHON ?= python3 # Python 3 executable

test: life.doctest life.test range.test

%.doctest:
	$(PYTHON) -m doctest $(@:.doctest=.py)

%.test:
	$(PYTHON) $(@:.test=_test.py) > $(@:.test=_test.out)
	diff -q $(@:.test=_test.out) $(@:.test=_test.correct)

clean:
	rm -rf *.out __pycache__
