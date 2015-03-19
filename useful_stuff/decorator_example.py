def dec(fn_or_dec_arg):
    if callable(fn_or_dec_arg):
        def wrapper(fn_arg):
            return '#dec#' + fn_or_dec_arg(fn_arg)
        return wrapper
    else:
        def fn_wrapper(fn):
            def wrapper(fn_arg):
                return '#dec#' + fn_or_dec_arg + fn(fn_arg)
            return wrapper
        return fn_wrapper


# @dec
# @dec('#dec_arg#')
def func(fn_arg):
    return fn_arg

# func = dec('#dec_arg#')(func) # @dec('#dec_arg#')
# func = dec(func) # @dec
print(func('#fn_arg#'))
