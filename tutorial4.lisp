;;; 22.01.2018
;;; https://www.cs.sfu.ca/CourseCentral/310/pwfong/Lisp/4/tutorial4.html

(defparameter *counter* 0 "Zähler, um etwas zu zählen")

(setf *counter* (1+ *counter*))

(print *counter*)

;; Exersice: global Stack abstraction

(defparameter *stack* () "Globaler Stack")

(defun stack-push (E)
  "Push Element E auf Stack"
  (push E *stack*))

(defun stack-pop ()
  "Pop element von Stack"
  (pop *stack*))

(stack-push '112ds)
(print *stack*)
(stack-pop)


;; Ex: encapsulated global stack-pop

(defparameter list-of-funcs nil "Liste mit Stack-Funktionen")

(setf list-of-funcs (let ((stack nil))
		      (list #'(lambda (E)
				(push E stack))
			    #'(lambda ()
				(pop stack)))))

(defparameter enc-stack-push (first list-of-funcs))
(defparameter enc-stack-pop (second list-of-funcs))

(funcall enc-stack-push '(1 2 3 4))
(funcall enc-stack-pop)


(defun make-counter ()
  "Neues Counter-Object erstellen"
  (let ((counter 0))
    (list #'(lambda ()
	      (incf counter))
	  #'(lambda ()
	      (setf counter 0)))))

(defun counter-increment (counter)
  (funcall (first counter)))

(defun counter-reset (counter)
  (funcall (second counter)))

(defparameter c1 (make-counter))

(counter-increment c1)
(counter-reset c1)

(defun make-stack ()
  "Neuen Stack"
  (let ((stack nil))
    (list #'(lambda (E)
	      (push E stack))
	  #'(lambda ()
	      (pop stack)))))

(defun stack-push (E stack)
  (funcall (first stack) E))

(defun stack-pop (stack)
  (funcall (second stack)))

(defparameter s1 (make-stack))

(stack-push "hdsafadsallo" s1)
(stack-pop s1)

