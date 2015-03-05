(require '[clojure.string :as st])

;; More interested in the hyperbinary problem than this one for the moment.
;; I'll work on it when I get some time.

(let [[x y] (st/split (read-line) #" ")]
  (for [line (repeatedly read-line) :while line]
    (loop [w (st/split line #".")]
      (cond
        (= (first w) '\n') nil ; '\n' is not a char
        (not= (first w) '.') (do
                               (println (first w))
                               (recur (rest w)))
      )))

