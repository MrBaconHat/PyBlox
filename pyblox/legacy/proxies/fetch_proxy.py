class FetchProxy:
    def __init__(self, func, *args):
        self._func = func
        self._args = args

    def __call__(self, **kwargs):
        return self._func(*self._args, **kwargs)

    def __await__(self):
        return self._func(*self._args).__await__()