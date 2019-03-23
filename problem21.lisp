(defun list-divisors (n)
  (list-divisors-aux n (ceiling (/ n 2)) nil))

(defun list-divisors-aux (n a L)
  "n ist die Zahl, für die getestet wird;
   a ist die Zahl, bei der gerade ist (von 1 bis n)
   L ist die Liste mit gefundenen Divisoren"
  (if (= a 0)
       L
       (if (= 0 (rem n a))
	   (list-divisors-aux n (1- a) (cons a L))
	   (list-divisors-aux n (1- a) L))))

(defun sum-divisors (n)
  (apply '+ (list-divisors n)))

(defun is-amicable-pair (a)
  "Is a and sum-divisors n amicable pair?
   Wenn ja return (a b)"
  (let ((b (sum-divisors a)))
    (if (and (= a (sum-divisors b)) (/= a b))
	(print b)
	nil)))

(defun sum-amicable-numbers (n)
  "Summe der amicablen Nummern bis n"
  (sum-amicable-numbers-aux n n nil))


(defun sum-amicable-numbers-aux (n a L)
  "Summe der amicablen Nummern bis n,
   gerade betrachetet Nummer a,
   Liste mit Ergebnissen L"
  (if (= a 1)
      (apply '+ L)
      (let ((b (is-amicable-pair a)))
	(if (null b)
	    (sum-amicable-numbers-aux n (1- a) L)
	    (if (or (find-if (lambda (x) (or (= x a) (= x b))) L) (> b n))
		(sum-amicable-numbers-aux n (1- a) L)
		(sum-amicable-numbers-aux n (1- a) (cons a (cons b L))))))))
