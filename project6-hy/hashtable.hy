;; note that `eqv?` in racket is like `==` in Python, and `eq?` is like `is`.
;; `assv` uses `eqv?` in racket, and `assq` uses `eq?`.
(defun assv (x ls)
  (if (empty? ls) False
    (let ((a (car ls)))
      (let ((aa (car a)))
        (if (= aa x)
          a
          (assv x (cdr ls)))))))

(defun assq (x ls)
  (if (empty? ls) False
    (let ((a (car ls)))
      (let ((aa (car a)))
        (if (is aa x)
          a
          (assq x (cdr ls)))))))

(defclass Hashtable ()
  ((__init__ 
     (lambda (self d)
       (let ((input-len (len d)))
         (setv self.m
               (if (zero? input-len) 11
                 (* input-len 2)))
         (setv self.n input-len)
         (setv self.data
               (list-comp '() (_ (range 0 self.m))))
         (for (k (.keys d))
              (assoc self k (. d [k]))))))

   (__getitem__ 
     (lambda (self key)
       (let ((hk (.hash self key)))
         (if (empty? (. self.data [hk]))
           (KeyError (.format "{} is not a valid key" key))
           (let ((v (for (e (. self.data [hk]))
                         (let ((k (car e))
                               (v (cdr e)))
                           (if (= key k)
                             v)))))
             (if v v
               (KeyError (.format "{} is not a valid key" key))))))))
    
    (__setitem__ 
      (lambda (self key value)
        (let ((alpha (/ (float (. self n)) (. self m))))
          (if (> alpha '0.5)
            (.__init__ self self))
          (let ((hk (.hash self key)))
            (let ((exists (assv key (. self.data [hk]))))
              (if exists
                (let ((i (.index (. self.data [hk]) exists)))
                  (assoc (. self.data [hk]) i `(~key . ~value)))
                (assoc self.data hk (cons 
                                      `(~key . ~value) 
                                      (. self.data [hk])))))))))

    (__delitem__
      (lambda (self key)
        (let ((alpha (/ (float (. self n)) (. self m))))
          (if (< alpha '0.25)
            (.__init__ self self))
          (let ((hk (.hash self key)))
            (let ((e (assv key (. self.data [hk]))))
              (if e
                (let ((i (.index (. self.data [hk]) e)))
                  (del (. self.data [hk] [i])))
                (KeyError (.format "{} is not a valid key." key))))))))

    (keys
      (lambda (self)
        (do
          (setv acc '())
          (for (chain self.data)
               (if-not (empty? chain)
                 (for (e chain)
                      (let ((k (car e))
                            (v (cdr e)))
                        (setv acc (cons k acc)))))))))
    
    (hash
      (lambda (self k)
        (% (hash k) (. self m))))))

(defmain (&rest args)
  (do
    (import tests)
    (setv D (dict-comp k (len k) (k (. tests some_words))))
    (setv T (Hashtable D))
    (.do_tests tests T)))

