(defun is-divisable (number divisor)
  (if (= 0 (rem number divisor))
      t
      nil))

(defun is-not-divisible-by-list (number list)
  "returns number if it is not divisible by any element in the list; otherwise returns nil"
  (if (null list)
       number
       (if (is-divisable number (car list))
       	  nil
       	  (is-not-divisible-by-list number (cdr list)))))

(defun list-of-primes (max)
  "Returns a list of primes up to max"
  (list-of-primes-aux max 2 '()))

(defun list-of-primes-aux (max current list)
  (if (< max current)
      list
      (let ((x (is-not-divisible-by-list current list)))
	(if (null x)
	    (list-of-primes-aux max (+ 1 current) list)
	    (list-of-primes-aux max (+ 1 current) (cons x list))))))

(defun num-to-digit-list (num)
  (loop for c across (write-to-string num) collect (digit-char-p c)))
  
(defun has-same-digits

(defun count-primes-with-replace (num primes-list)
