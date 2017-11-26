def debug(f):
    # TODO it is probably best to find out if `f` is a function, a method, a
    # classmethod or a staticmethod.
    #
    # That way we can correctly print a sensible `args` without potentially
    # ending in an infinite loop.

    def wrapper(*args, **kwargs):
        from os import getenv
        debug = getenv('DEBUG')
        from datetime import datetime as dt

        if debug:
            start = dt.now()
            print('\n\n\n')
            print('  =============DEBUG=============')
            print('      args to f = %s' % repr(args[1:]))  # ignore self
            print('    kwargs to f = %s' % str(kwargs))
            print('       called f   %s' % start)

        res = f(*args, **kwargs)

        if debug:
            end = dt.now()
            print('    return of f = %s' % repr(res))
            print('       timeit f   %s' % (end - start))
            print('  =============GUBED============')
            print('\n\n\n')

        return res

    return wrapper
