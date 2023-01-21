; Write your solutions for smallest, remove, and sort below

(define (smallest l val)
  (cond
    ((null? l) val)
    ((< (car l) val) (smallest (cdr l) (car l)))
    (else (smallest (cdr l) val))))

(define (remove l val)
  (cond
    ((null? l) l)
    ((eq? (car l) val) (cdr l))
    (else (cons (car l) (remove (cdr l) val)))))

(define (sort l)
  (if (null? l) l (let ((small (smallest l (car l)))) (cons small (sort (remove l small))))))

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

; smallest tests
(display "running smallest tests\n")
(test 'smallest smallest '((1 2 3 4 5) 2) 1)
(test 'smallest smallest '((4 3 7) 3) 3)
(test 'smallest smallest '((4 3 7) 5) 3)

; remove tests
(display "running remove tests\n")
(test 'remove remove '((1 2 3 4 5) 2) '(1 3 4 5))
(test 'remove remove '((1 2 3 4 5) 6) '(1 2 3 4 5))
(test 'remove remove '(() 6) '())

; sort tests
(display "running sort tests\n")
(test 'sort sort '((6 4 5 3 9 3)) '(3 3 4 5 6 9))
(test 'sort sort '(()) '())
