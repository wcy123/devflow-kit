
```
(/define-syntax get-ctv
  (lambda (e)
    (syntax-case e ()
      ((_ k)
       (identifier? #'k)
       (lambda (lookup)
         (let ((v (lookup #'k)))
           #`(quote #,v)))))))
```
