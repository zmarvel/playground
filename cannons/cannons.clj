(defn word-collision
  [w1 w2]
  (let [lletters (reduce #(assoc %1 %2 (inc (get %1 %2 0))) {} w1)
        rletters (reduce #(assoc %1 %2 (inc (get %1 %2 0))) {} w2)
        ldiff (reduce #(assoc %1 (key %2) (- (val %2) (rletters (key %2) 0)))
                      {}
                      lletters)
        rdiff (reduce
                #(assoc %1 (key %2) (- (val %2) (lletters (key %2) 0)))
                {}
                rletters)
        ltotals (filter #(pos? (val %1)) ldiff)
        rtotals (filter #(pos? (val %1)) rdiff)]
      [ltotals rtotals]))

(doseq [line (take-while (partial not= ":q") (repeatedly read-line))]
  (let [[lword rword] (.split line " ")
        [left right] (word-collision lword rword)
        lscore (apply + (vals left))
        rscore (apply + (vals right))]
    (cond
      (> lscore rscore) (println "Left wins. " lscore rscore)
      (< lscore rscore) (println "Right wins. " lscore rscore)
      :else (println "It's a tie. " lscore rscore))
    (println (into (keys left) (keys right)))))
