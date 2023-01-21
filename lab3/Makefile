SCHEME ?= plt-r5rs # Scheme executable

test: lists.errtest sort.errtest

%.errtest:
	$(SCHEME) $(@:.errtest=.scm) > $(@:.errtest=.out)
	! (grep -v '^running' $(@:.errtest=.out) | grep -v '^pass')

clean:
	rm -rf *.out
