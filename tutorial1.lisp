;;; 22.01.2018
;;; https://www.cs.sfu.ca/CourseCentral/310/pwfong/Lisp/1/tutorial1.html

(defun fib (N)
  "Fibonacci Nummer"
  (if (<= N 1)
      1
      (+ (fib (1- N)) (fib (- N 2)))))

(defun binominal (N R)
  "Binominal Koeffizient"
  (if (or (zerop N) (zerop R))
      1
      (+ (binominal (- N 1) (- R 1)) (binominal (- N 1) R))))

(defun find-biggest (x)
  "Finde die grˆﬂte Zahl"
  (if (null (rest x))
      (first x)
      (let ((_first (first x))
	    (_second (find-biggest (rest x))))
	(if (>= _first _second)
	    _first
	    _second))))

(defun len-list (x)
  "L‰nge einer Liste"
  (if (null x)
      0
      (+ 1 (len-list (rest x)))))

(defun summe (x)
  (if (null x)
      0
      (+ (first x) (summe (rest x)))))

(defun letztes (x)
  "Letztes Element in Liste"
  (if (null (rest x))
      (first x)
      (letztes (rest x))))

(defun is-member (E L)
  "Ist Element in Liste?"
  (cond
    ((null L) nil)
    ((equal E (first L)) t)
    (t (is-member E (rest L)))))

(print (is-member 'scheiﬂ '(heute ist ein scheiﬂ Tag lol)))

(defun anh‰ngen (X Y)
  (if (null X)
      Y
      (cons (first X) (anh‰ngen (rest X) Y))))

(print (anh‰ngen '(a b c) '(c d e)))

(defun auﬂer-letztes (X)
  "Returns all Elements but the last one"
  (if (null (rest X))
      ()
      (cons (first X) (auﬂer-letztes (rest X)))))

(print (auﬂer-letztes '(1 2 3 4 5 6 7 8 9 10)))


(defun menge-differenz (X Y)
  "Differenz von 2 Mengen."
  (cond
    ((null X) ())
    ((member (first X) Y) (menge-differenz (rest X) Y))
    (t (cons (first X) (menge-differenz (rest X) Y)))))

(defun men (X Y)
  (union (menge-differenz X Y) (menge-differenz Y X)))

(print (men '(1 2 3 4 5 6 7) '(5 6 7 8 9 10)))

(defun menge-union (X Y)
  "Vereint 2 Mengen"
  (cond
    ((null X) Y)
    ((member (first X) Y) (menge-union (rest X) Y))
    (t (menge-union (rest X) (cons (first X) Y)))))

(print (menge-union '(1 2 3 4 5 6) '(4 5 6 7 8 9 10)))
