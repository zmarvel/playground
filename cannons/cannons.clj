(ns cannons.core)

(defn word-collision
  [w1 w2]
    [(reduce (fn [x] (.replaceFirst w2 (.toString x) "")) w1)
     (reduce (fn [x] (.replaceFirst w1 (.toString x) "")) w2)])

(doseq [line (take-while (partial not= ":q") (repeatedly read-line))]
  (let [[left-word right-word] (.split line " ")
        [left-score right-score] (word-collision left-word right-word)]
    (println (into left-score right-score))
    (println (count left-score) (count right-score))))
