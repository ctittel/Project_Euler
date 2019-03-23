;;; 22.01.2018
;;; https://www.cs.sfu.ca/CourseCentral/310/pwfong/Lisp/2/tutorial2.html

(defun list-append (X Y)
  (if (null X)
      Y
      (cons (first X) (list-append (rest X) Y))))

(defun reverse-slow (L)
  (if (null (rest L))
      L
      (list-append (reverse-slow (rest L)) (list (first L)))))

(print (reverse-slow '(1 2 3 4 5 6 7 8 9)))


(defun list-reverse-aux (L A)
  "Append list A to the reversal of List L"
  (if (null L)
      A
      (list-reverse-aux (rest L) (cons (first L) A))))

(defun list-reverse (L)
  "Reverse List L"
  (list-reverse-aux L nil))

(print (list-reverse '(1 2 3 4 5 6 7 8)))

(defun factorial-slow (n)
  (if (<= n 1)
      1
      (* n (factorial-slow (1- n)))))

(defun factorial-fast-aux (n a)
  (if (>= 1 n)
      a
      (factorial-fast-aux (1- n) (* n a))))

(defun factorial-fast (n)
  (factorial-fast-aux n 1))

(print (factorial-fast 30))
(print (factorial-slow 30))


(defun triangular-fast-aux (n a)
  (if (= 1 n)
      (1+ a)
      (triangular-fast-aux (1- n) (+ n a))))

(defun triangular-fast (n)
  (triangular-fast-aux n 0))

(print (triangular-fast 3))


(defun fast-power-aux (a n m)
  "a hoch n mal m"
  (if (= n 1)
      (* a m)
      (fast-power-aux a (1- n) (* m a))))

(defun fast-power (a n)
  "a hoch n"
  (fast-power-aux a n 1))

(print (fast-power 10 3))


(defun fast-list-length-aux (L n)
  "Länge der Liste L plus n"
  (if (null L)
      n
      (fast-list-length-aux (rest L) (1+ n))))

(defun fast-list-length (L)
  (fast-list-length-aux L 0))

(print (fast-list-length '(1 2 3 4 5 6 7 8 9 10 11 12 13)))

(defun doubl (x)
  (* 2 x))

(defun repeat-transformation (F N X)
  "Wiederhole das Anwenden von F auf X n-mal"
  (if (zerop N)
      x
      (repeat-transformation F (1- N) (funcall F X))))

(print (repeat-transformation (function doubl) 4 1))

(defun prepend-blah (L) (cons 'blah L))

(print (repeat-transformation #'prepend-blah 10 nil))

(print (repeat-transformation #'(lambda (L) (cons 'blah L)) 10 nil))


(defun apply-func-list (f p)
  "Liste mit Funktionen f auf Liste mit Parametern p anwenden."
  (if (null f)
      p
      (apply-func-list (rest f) (funcall (first f) p))))

(defun apply-func-list-rev (f p)
  "Liste mit Funktionen f auf Liste mit Parametern p anwenden, in umgekehrter Reihenfolge."
  (if (null f)
      p
      (funcall (first f) (apply-func-list-rev (rest f) p))))

(print (apply-func-list-rev (list #'doubl #'list-length #'rest) '(1 2 3 4 5 6)))

(print (apply-func-list-rev (list #'(lambda (x) (* 10 x))
				  #'fourth)
			    '(10 20 30 40 50)))

(print (apply-func-list-rev (list #'third #'second) '((1 2) (3 4 5) (6))))

(print (apply-func-list-rev (list #'(lambda (x) (- 10 x)) #'list-length) '(a b c d e f)))

(print (apply-func-list-rev (list #'list #'list) 'blah))

(defun mapfirst (F L)
  "Funktion F wird auf jedes Element von L angewendet, das Ergebnis ist eine Liste"
  (if (null L)
      nil
      (cons (funcall F (first L)) (mapfirst F (rest L)))))

(print (mapfirst #'doubl '(1 2 3 4 5)))

(print (mapfirst #'(lambda (x) (* x x)) '(1 2 3 4 5 6 7 8 9 10)))
(print (mapcar #'(lambda (x) (* x x)) '(1 2 3 4 5 6 7 8 9 10)))

(print (find-if #'(lambda (x) (>= (length x) 3)) '((1) (1 2) (1 2 3) (1 2 3 4))))

(print (find-if #'(lambda (x) (evenp (length x))) '((1) (1 2) (1 2 3) (1 2 3 4))))

(print (remove-if #'(lambda (x) (zerop (rem x 2))) '(1 2 3 4 5 6 7 8 9 10 11)))


(defun list-difference (A B)
  "Liste mit Elementen, die entweder nur in A oder nur B vorkommen."
  (remove-if #'(lambda (x)
		 (and
		  (find-if #'(lambda (y) (eq x y)) A)
		  (find-if #'(lambda (y) (eq x y)) B)))
	     (list-append A B)))

(print (list-difference '(1 2 3 4 5) '(3 4 5 6 7 8 9 10)))

(floor 17 5)

(defun list-min-max-aux (L min max)
  "Liefert minimum und maximum einer Liste, wenn diese kleiner bzw. größer als min bzw. max sind"
  (if (null L)
      (values min max)
      (list-min-max-aux (rest L)
			(if (< (first L) min)
			    (first L)
			    min)
			(if (> (first L) max)
			    (first L)
			    max))))
  
  
(defun list-min-max (L)
  "Liefert minimum und maximum einer Liste L."
  (list-min-max-aux (rest L) (first L) (first L)))

(print (list-min-max '(1 2 3 4 5 0 7 8 9 10 100 -1 2 4 300 2 3 -20 2 1 1 2)))

(list-min-max '(1 2 3 4 5 0 7 8 9 10 100 -1 2 4 300 2000000 3 -20 2 1 1 2))
