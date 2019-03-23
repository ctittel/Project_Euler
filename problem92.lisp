(defun digits-square (x)
  (digits-square-aux x 0))

(defun digits-square-aux (x sum)
  (if(= 0 x)
     sum
     (let ((digit (rem x 10)))
       (digits-square-aux (floor x 10) (+ sum (* digit digit))))))

(defun chain-ending (x)
  (let((i (digits-square x)))
    (cond((= 1 i) 1)
	 ((= 89 i) 89)
	 (t (chain-ending i)))))

(defun combine-lists (a b)
  (if(null a)
     b
     (combine-lists (rest a) (cons (first a) b))))

(defun cons-to-every-list (e L)
  (mapcar #'(lambda (x) (cons e x)) L))

(defun repeat (e n)
  "Repeat Element e n-mal"
  (if(= 0 n)
     '()
     (cons e (repeat e (1- n)))))

(defun lists-with-sum (sum len)
  "Ergibt eine Liste, wobei verschiedene verteilungen vorkommen
   die summe ist immer sum"
  (cond  ((= 0 sum) (list (repeat 0 len)))
	 ((= 1 len) (list (list sum)))
	 (t (lists-with-sum-aux sum len 0))))

(defun lists-with-sum-aux (sum len vorne)
  "Vorne ist die Zahl, die in dieser Iteration vorne steht"
  (cond ((= sum vorne) (list (cons vorne (repeat 0 (1- len)))))
	 (t (combine-lists (cons-to-every-list vorne (lists-with-sum (- sum vorne) (1- len)))
			   (lists-with-sum-aux sum len (1+ vorne))))))

(defun factorial (n &optional (sum 1))
  (if(= 0 n)
     sum
     (factorial (1- n) (* n sum))))

(defun permutation-with-repetition (L fact-sum)
  (/ fact-sum (sum-factorials L)))

(defun sum-factorials (L &optional (sum 1))
  (if(null L)
     sum
     (sum-factorials (rest L) (* sum (factorial (first L))))))

(defun count-chain-ending (ending-at l d)
  "Zähle Zahlen, dere Ketten bei ending-at enden,
   die Zahl hat l Stellen,
   es stehen d Digits zur verfügung"
  (defparameter *oben* (factorial l))
  (count-chain-ending-aux ending-at l d 0 (lists-with-sum l d)))

(defun count-chain-ending-aux (ending-at l d sum L)
  (cond ((null L) sum)
	((= ending-at chain-ending(list-to-num (first L)))
	 (count-chain-ending-aux ending-at l d (+ sum (permutation-with-repetition (first L) *oben*)) (rest L)))
	(t (count-chain-ending-aux l d sum (rest L)))))

(defun list-to-num (L &optional (sum 0) (erstes 0))
  (if(null L)
     sum
     (list-to-num (rest L) (+ sum (* (first L) erstes)) (1+ erstes))))
