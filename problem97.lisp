(defun last-digits (n num)
  (rem num (expt 10 n)))

(defun mult-n-times-x (num n x)
  "Multipliziere num mit x hoch n"
  (if(= 0 n)
     num
     (mult-n-times-x (last-digits 10 (* num x)) (1- n) x)))

(defun problem97 ()
  (print (1+ (mult-n-times-x 28433 7830457 2))))
