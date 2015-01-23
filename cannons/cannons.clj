(ns cannons.core)

(defn word-collision
  [w1 w2]
  (let [left-letters (reduce
                       (fn [acc x] (assoc acc x (inc (get acc x 0))))
                       {}
                       w1)
        right-letters (reduce
                        (fn [acc x] (assoc acc x (inc (get acc x 0))))
                        {}
                        w2)]
    (merge-with (fn [x y]
                  (let [diff (- x y)]
                    (cond
                      (> diff 0) :left
                      (< diff 0) :right
                      :else diff)))
                left-letters
                right-letters)))

(doseq [line (take-while (partial not= ":q") (repeatedly read-line))]
  (let [[left-word right-word] (.split line " ")
        result (word-collision left-word right-word)]
    (println result)))
