(defun len-num (num &optional (sum 0))
  (if(= 0 num)
     sum
     (len-num (floor num 10) (1+ sum))))

(defun is-palindromic-aux (num len)
  (if(>= 1 len)
     t
     (let ((first-digit (num-first num len))
	   (last-digit (num-last num))
	   (new-num (middle-of-num num len)))
       (if(= first-digit last-digit)
	  (is-palindromic-aux new-num (- len 2))
	  nil))))

(defun num-first (num len)
  (floor num (expt 10 (1- len))))

(defun num-last (num)
  (rem num 10))

(defun middle-of-num (num len)
  (floor (rem num (expt 10 (1- len))) 10))

(defun is-palindromic (num)
  (is-palindromic-aux num (len-num num)))

(defun reverse-num (num &optional (len (len-num num)) (new-num 0))
  (if (= 0 len)
      new-num
      (reverse-num (floor num 10) (1- len) (+ (* 10 new-num) (rem num 10)))))

(defun reverse-add (num)
  (+ num (reverse-num num)))

(defun becomes-palindromic-within (num i)
  "Wird num innerhalb von i Iterationen palindromic?"
  (if(= 0 i)
     nil
     (let((new-num (reverse-add num)))
       (if(is-palindromic new-num)
	  t
	  (becomes-palindromic-within new-num (1- i))))))

(defun is-lychrel-num (num)
  (if(becomes-palindromic-within num 50)
     0
     1))

(defun count-lychrel-nums-from (n &optional (sum 0))
  (if(= 0 n)
     sum
     (count-lychrel-nums-from (1- n) (+ sum (is-lychrel-num n)))))
