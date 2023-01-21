; Write your solutions for list-append, deep-reverse, and contains
; below

(define (list-append list-1 list-2)
  (if (null? list-1) list-2 (cons (car list-1) (list-append (cdr list-1) list-2))))

(define (deep-reverse l)
  (cond
    ((null? l) l)
    ((list? (car l)) (list-append (deep-reverse (cdr l)) (list (deep-reverse (car l)))))
    ;((list? (car l)) (list-append (deep-reverse (cdr l)) (deep-reverse (car l))))
    (else (list-append (deep-reverse (cdr l)) (list (car l))))))

(define (contains l val)
  (cond
    ((null? l) #f)
    ((eq? (car l) val) #t)
    (else (contains (cdr l) val))))

; Test code
(define (assert-equal x y test)
  (if (not (equal? x y))
      (begin
        (display "Error for test ")
        (write test)
        (display ": ")
        (write x)
        (display " not equal? to ")
        (write y)
        (newline))
      (display "pass\n")))

(define (quotify args)
  (map (lambda (x) (list 'quote x)) args))

(define (test name func args expect)
  (assert-equal (apply func args) expect (cons name (quotify args))))

; append tests
(display "running list-append tests\n")
(test 'list-append list-append '((1 2) (2 3)) '(1 2 2 3))
(test 'list-append list-append '(() (2 3)) '(2 3))
(test 'list-append list-append '(() ()) '())

; reverse tests
(display "running deep-reverse tests\n")
(test 'deep-reverse deep-reverse '((1 2 3 4 5)) '(5 4 3 2 1))
(test 'deep-reverse deep-reverse '(((2 4) (1 3))) '((3 1) (4 2)))
(test 'deep-reverse deep-reverse '((1)) '(1))

; contains tests
(display "running contains tests\n")
(test 'contains contains '((1 2 3 4 5) 3) #t)
(test 'contains contains '((1 2 3 4 5) 6) #f)
(test 'contains contains '(() 6) #f)
