(defun is_prime (n)
  (cond
	((= 2 n) t)
	((= 3 n) t)
	((evenp n) nil)
	(t (loop for i from 3 to (isqrt n) by 2
			 never (zerop (mod n i))))
	)

  )

(defun primes_to (n)
  
  (if (<= n 1)
	nil
	(if (is_prime n)
	  (append (primes_to (- n 1)) (list n))
      (primes_to (- n 1))
	)
  )
)
