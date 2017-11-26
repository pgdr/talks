def debug(f):
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
