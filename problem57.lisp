(defun expansion-aux (n)
  (if(= 0 n)
     2
     (+ 2 (/ 1 (expansion (1- n))))))

(defun expansion (n)
  (+ 1 (/ 1 (expansion-aux n))))
	  
