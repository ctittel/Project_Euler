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

(defun is-abundant (n)
  (if (< n (sum-divisors n))
      t
      nil))

(defun list-abundant-numbers (n)
  "Liste mit abundant nummern bis n"
  (list-abundant-numbers-aux n n nil))

(defun list-abundant-numbers-aux (n a L)
  "n = Endzahl
   a = Zahl gerade
   L = Ergebnissliste"
  (cond
    ((= 1 a) L)
    ((is-abundant a) (list-abundant-numbers-aux n (1- a) (cons a L)))
    (t (list-abundant-numbers-aux n (1- a) L))))

(defun is-abundant-sum (n L)
  "Zahl n
   Liste mit abundanten Zahlen L"
  (if(null L)
     nil
     (let ((diff (- n (first L))))
       (cond ((< diff 0) nil)
	     ((is-in-list diff L) t)
	     (t (is-abundant-sum n (rest L)))))))

(defun is-in-list (n L)
  "Ist n in Liste L?
   L ist nach der größe geordnet"
  (cond ((= n (first L)) t)
	((< n (first L)) nil)
	(t (is-in-list n (rest L)))))

(defun sum-of-non-abundant-sums (n L)
  "n: Bis zu welcher Zahl
   L: Liste abundanter Zahlen"
  (sum-of-non-abundant-sums-aux n n L 0))

(defun sum-of-non-abundant-sums-aux (n a L sum)
  "Summiert alle nicht abundanten Summen <= a"
  (if(= a 0)
     sum
     (if(is-abundant-sum (print a) L)
	(sum-of-non-abundant-sums-aux n (1- a) L sum)
	(sum-of-non-abundant-sums-aux n (1- a) L (+ sum a)))))

(print (sum-of-non-abundant-sums 28123 (print (list-abundant-numbers 28123))))
