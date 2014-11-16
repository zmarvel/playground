from hy import HyCons, HyExpression, HyFloat
from hy.core.language import cons, is_integer, is_nil, is_zero, range

def assv(x, ls):
    if is_nil(ls):
        _hy_anon_var_2 = False
    else:
        def _hy_anon_fn_2():
            a = ls[0L]

            def _hy_anon_fn_1():
                aa = a[0L]
                return (a if (aa == x) else assv(x, ls[1L:]))
            return _hy_anon_fn_1()
        _hy_anon_var_1 = _hy_anon_fn_2()
    _hy_anon_var_2 = _hy_anon_var_1
    return _hy_anon_var_2

def assq(x, ls):
    if is_nil(ls):
        _hy_anon_var_4 = False
    else:
        def _hy_anon_fn_5():
            a = ls[0L]

            def _hy_anon_fn_4():
                aa = a[0L]
                return (a if (aa is x) else assq(x, ls[1L:]))
            return _hy_anon_fn_4()
        _hy_anon_var_3 = _hy_anon_fn_5()
    _hy_anon_var_4 = _hy_anon_var_3
    return _hy_anon_var_4


class Hashtable:

    def __init__(self, d):

        def _hy_anon_fn_7():
            input_len = len(d)
            self.m = (11L if is_zero(input_len) else (input_len * 2L))
            self.m
            self.n = input_len
            self.n
            self.data = [None for range in 0L]
            self.data
            for k in d.keys():
                self[k] = d[k]
        return _hy_anon_fn_7()

    def __getitem__(self, key):

        def _hy_anon_fn_11():
            hk = self.hash(key)
            if is_nil(self.data[hk]):
                _hy_anon_var_6 = KeyError(u'{} is not a valid key'.format(key))
            else:
                def _hy_anon_fn_10():
                    for e in self.data[hk]:

                        def _hy_anon_fn_9():
                            k = e[0L]
                            v = e[1L:]
                            return (v if (key == k) else None)
                        _hy_anon_fn_9()
                    v = None
                    return (v if v else KeyError(u'{} is not a valid key'.format(key)))
                _hy_anon_var_5 = _hy_anon_fn_10()
                _hy_anon_var_6 = _hy_anon_var_5
            return _hy_anon_var_6
        return _hy_anon_fn_11()

    def __setitem__(self, key, value):

        def _hy_anon_fn_16():
            alpha = (float(self.n) / self.m)
            (self.__init__(self) if (alpha > HyFloat(0.5)) else None)

            def _hy_anon_fn_15():
                hk = self.hash(key)

                def _hy_anon_fn_14():
                    exists = assv(key, self.data[hk])
                    if is_nil(self.data[hk]):
                        self.data[hk] = HyExpression([])
                        _hy_anon_var_9 = None
                    else:
                        if exists:

                            def _hy_anon_fn_13():
                                i = self.data[hk].index(exists)
                                self.data[hk][i] = HyCons(key, value)
                            _hy_anon_var_8 = _hy_anon_fn_13()
                        else:
                            self.data[hk] = cons(HyCons(key, value), self.data[hk])
                            _hy_anon_var_7 = None
                            _hy_anon_var_8 = _hy_anon_var_7
                        _hy_anon_var_9 = _hy_anon_var_8
                    return _hy_anon_var_9
                return _hy_anon_fn_14()
            return _hy_anon_fn_15()
        return _hy_anon_fn_16()

    def __delitem__(self, key):

        def _hy_anon_fn_21():
            alpha = (float(self.n) / self.m)
            (self.__init__(self) if (alpha < HyFloat(0.25)) else None)

            def _hy_anon_fn_20():
                hk = self.hash(key)

                def _hy_anon_fn_19():
                    e = assv(key, self.data[hk])
                    if e:

                        def _hy_anon_fn_18():
                            i = self.data[hk].index(e)
                            del self.data[hk][i]
                        _hy_anon_var_10 = _hy_anon_fn_18()
                    else:
                        _hy_anon_var_10 = KeyError(u'{} is not a valid key.'.format(key))
                    return _hy_anon_var_10
                return _hy_anon_fn_19()
            return _hy_anon_fn_20()
        return _hy_anon_fn_21()

    def keys(self):
        acc = HyExpression([])
        for chain in self.data:
            if (not is_nil(chain)):
                for e in chain:

                    def _hy_anon_fn_23():
                        k = e[0L]
                        v = e[1L:]
                        acc = cons(k, acc)
                        return acc
                    _hy_anon_fn_23()
                _hy_anon_var_11 = None
            else:
                _hy_anon_var_11 = None
    hash = (lambda self, k: (hash(k) % self.m))

def main(*args):
    import tests
    D = {k: len(k) for k in tests.some_words}
    T = Hashtable(D)
    return tests.do_tests(T)
if (__name__ == u'__main__'):
    import sys
    G_1235 = main(*sys.argv)
    _hy_anon_var_12 = (sys.exit(G_1235) if is_integer(G_1235) else None)
else:
    _hy_anon_var_12 = None
