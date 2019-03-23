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

(defun list-of-endings (to &optional (L nil) (now 1))
  (cond ((< to now) L)
	(t (list-of-endings to (cons (chain-ending now) L) (1+ now)))))

(defun reverse-list (L)
  (reverse-list-aux L nil))

(defun reverse-list-aux (a b)
  (if(null a)
     b
     (reverse-list-aux (rest a) (cons (first a) b))))

(defun count-chains-aux (end jetzt sum L)
  (cond ((= jetzt end) sum)
	((= 89 (nth (1- (digits-square jetzt)) L)) (count-chains-aux end (1+ jetzt) (1+ sum) L))
	(t (count-chains-aux end (1+ jetzt) sum L))))

(defun count-chains ()
  (count-chains-aux 10000000 1 0 (print (reverse-list (list-of-endings (* 7 9 9))))))

