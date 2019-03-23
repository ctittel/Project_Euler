(defun minimal-solution (D &optional (x 2))
  (let ((quotient (/ (1- (* x x)) D)))
    (if(not (is-integer quotient))
       (minimal-solution D (1+ x))
       (let ((y 


(defun is-integer (num)
  (if(equal 'integer (first (type-of (1+ num))))
     t
     nil))
		    
