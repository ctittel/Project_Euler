;;; 22.01.2018
;;; Project Euler Problem 12
;;; Triangel-Number mit mehr als 500 Divisoren gesucht

;; Laut Wikipedia:
;; n:    Zahl
;; p_k:  Prime-Faktoren
;; v_k:  wie oft Faktor vorkommt

;; n = (p_1)^(v_1) * (p_2)^(v_2) ... * (p_k)^(v_k)

;; Dann ist die Nummer der Positiven Divisoren:

;; d(n) = (v_1 + 1) * (v_2 + 1) ... * (v_k + 1)

;; Außerdem:
;; d(n) < 2 * sqrt(n)
;; 250^2 => n ist größer als 62500

(defparameter *primes* (2 3) "Liste mit Primzahlen")
(defparameter *primes-calculated-to* 3 "Bis wohin wurden Primes berechnet")
(defparameter *largest-prime* 1)

(defun reverse-list (L)
  (reverse-list-aux L nil))
  
(defun reverse-list-aux (A B)
  "Erstes Element von A wird an B angehängt"
  (if (null A)
      B
      (reverse-list-aux (rest A) (cons (first A) B))))

(defun calc-primes (calculate-to)
  (when (> calculate-to *primes-calculated-to*)
    (setf *primes* (reverse-list *primes*))
    (print "Calculating new Prime Numbers")
    (calc-primes-aux calculate-to (1+ *primes-calculated-to*))
    (setf *primes-calculated-to* calculate-to)
    (setf *largest-prime* (first *primes*))
    (setf *primes* (reverse-list *primes*)))
  (if (> calculate-to *primes-calculated-to*)
      (calc-primes (+ calculate-to 100))))

(defun calc-primes-aux (calculate-to calc-now)
  "Berechne Primes bis calculate-to, in dieser iteration calc-now"
  (unless (< calculate-to calc-now)
    (print (list "Berechne Primes bis " calculate-to "jetzt gerade bei " calc-now))
    (when (null (find-if #'(lambda (x) (zerop (rem calc-now x))) *primes*))
      (setf *primes* (cons calc-now *primes*)))
    (calc-primes-aux calculate-to (1+ calc-now))))
	  
      
(init-primes)
(calc-primes 200000)
(print *primes*)

(defun init-primes ()
  (setf *primes* '(2 3))
  (setf *primes-calculated-to* 3)
  (calc-primes 100))


(defun how-often-in (X I sum)
  "How often is I in X?"
  (if (= (rem X I) 0)
      (how-often-in (/ X I) I (1+ sum))
      sum))
  
(defun find-prime-divs (X)
  "Liste mit den Primfaktoren und deren Häufigkeit von x (p_k v_k)"
  (if (>= X *largest-prime*)
      (calc-primes X)
  (find-prime-divs-aux X 0 nil)))


(defun find-prime-divs-aux (X N L)
  "Zahl X, Primfaktor Nummer N, Liste mit Faktoren L (p_k v_k)"
  (let (( _L (if (= (rem X (nth N *primes*)) 0)
		 (cons (list (nth N *primes*) (how-often-in X (nth N *primes*) 0)) L)
		 L)))
    (if (> (nth (1+ N) *primes*) X)
	_L
	(find-prime-divs-aux X (1+ N) _L))))
	
(find-prime-divs 220)


(defun num-of-divs (X)
  "Anzahl der Divisoren der Zahl X"
  (num-of-divs-aux (find-prime-divs X) 1))


(defun num-of-divs-aux (L divs)
  "Nimmt das 2te element vom ersten der Liste, addiert 1 und multipliziert es zu divs"
  (if (null L)
      divs
      (num-of-divs-aux (rest L)
		       (* divs (1+ (second (first L)))))))

(defun problem12 (divs)
  "Finde die erste Dreiecksnummer mit mehr als divs Divisoren"
  (print (problem12-aux divs 1 1)))

(defun problem12-aux (divs N num)
  "divs = anz benötigter Divisoren, Nte Dreiecksnummer, Dreicksnummer num"
  (if (< divs (num-of-divs num))
      (list "Dreiecksnummer = " num "Anz Divisoren = " (num-of-divs num))
      (problem12-aux divs (1+ N) (+ num N 1))))

(problem12 500)
(find-prime-divs 1121)
(num-of-divs 112134)
(dribble "output.txt")
(print *primes*)
