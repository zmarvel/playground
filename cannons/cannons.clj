(ns app.core
  (:require clojure.set))

(defn word-collision
  "I don't do a whole lot."
  [w1 w2]
  (clojure.set/union
    (set (map (fn [x] (when (not (.contains w2 (.toString x))) x)) w1))
    (set (map (fn [x] (when (not (.contains w1 (.toString x))) x)) w2))))

(defn main
  []
  (println (word-collision "hill" "bill")))
