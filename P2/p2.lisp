(defun even_fibs_less_4mil (s1 s2)
  (if (> s2 4000000)
	0
    (if (= (mod s2 2) 0)
	  (+ s2 (even_fibs_less_4mil s2 (+ s1 s2)))
	  (even_fibs_less_4mil s2 (+ s1 s2))
	  )
	)
)
