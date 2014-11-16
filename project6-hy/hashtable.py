class Hashtable:
    def __init__(self, dict):
        input_len = len(dict)
        self.m = (input_len) * 2 if input_len > 0 else 11
        self.n = input_len
        self.data = [None for _ in range(0, self.m)]
        for k in dict.keys():
            self[k] = dict[k]

    def __getitem__(self, key):
        """Find a key in the hash table and return its associated value. If the
        key does not exist in the table, raise a KeyError."""
        
        h_k = self.hash(key)
        if not self.data[h_k] is None:
            for k, v in self.data[h_k]:
                if key == k:
                    return v
        KeyError("{} is not a valid key.".format(key))

    def __setitem__(self, key, value):
        """Given a key and a value, set the cell at that key in the hash table
        to that value. 
        
        Note that we have to make sure the item isn't already there, and note 
        that if the 'load' on the table is over 1/2, we're going to double its 
        size.
        """
        alpha = float(self.n) / self.m
        if alpha > 0.5:
            self.__init__(self)
        
        h_k = self.hash(key)
        if self.data[h_k] is None:
            self.data[h_k] = list()
        else:
            exists = filter(lambda t: t[0] == key, self.data[h_k])
            if exists:
                i = self.data[h_k].index(exists[0])
                self.data[h_k][i] = (key, value)
                return
        
        self.data[h_k].append((key, value))



    def __delitem__(self, key):
        """Given a key, find it in the hash table and delete it. 
        
        Note that if the 'load' on the table is under 1/4, we're going to reduce
        the table to half its size.
        """

        alpha = float(self.n) / self.m
        if alpha < 0.25:
            self.__init__(self)
        h_k = self.hash(key)
        for k, v in self.data[h_k]:
            if k == key:
                self.data[h_k].remove((k, v))
                return
        KeyError("{} is not a valid key.".format(key))

    def keys(self):
        return [k for chain in self.data if not chain is None for k, v in chain]

    def hash(self, k):
        return hash(k) % self.m

if __name__ == '__main__':
    import tests

    D = dict([(k, len(k)) for k in tests.some_words])
    T = Hashtable(D)
    tests.do_tests(T)
