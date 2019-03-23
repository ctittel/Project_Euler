(defun read-file-as-lines (filename)
  "Read file into a list of lines."
  (with-open-file (in filename)
    (loop for line = (read-line in nil nil)
      while line
      collect line)))

(defun line-as-list (line)
  "Read all objects from the line as a list."
  (read-from-string (concatenate 'string "(" line ")")))

(defun get-numbers ()
  (mapcar #'line-as-list (read-file-as-lines "./p067_triangle.txt")))

(defun tuple-below (n L)
  "Position n
   Below Line L"
  (list (nth n L) (nth (1+ n) L)))

(defun get-biggest (tu)
  "Get biggest number from Tuple tu"
  (let ((erstes (first tu))
	(zweites (second tu)))
    (if(> erstes zweites)
       erstes
       zweites)))

(defun reverse-list(a &optional (b nil))
  (if(null a)
     b
     (reverse-list (rest a) (cons (first a) b))))

(defun combine-lines(oben unten &optional (L nil))
  (if(null oben)
     (reverse-list L)
     (combine-lines (rest oben)
		    (rest unten)
		    (cons (+ (first oben)
			     (get-biggest (tuple-below 0 unten))) L))))

(defun get-biggest-sum (P L)
  "P Liste mit Listen, aktuelle ist ganz oben
   L linie darunter (nicht in P)"
  (if(null (rest P))
     (print (list P L))
     (get-biggest-sum (rest P) (combine-lines (first P) L))))

(defun problem67 ()
  (let ((P (reverse-list (get-numbers))))
    (get-biggest-sum (rest P) (first P))))
