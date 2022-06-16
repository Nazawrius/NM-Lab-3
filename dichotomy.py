def dichotomy_method(f, a, b, eps):
    x = (a + b) / 2
    _x = a
    n = 0
    while(abs(x - _x) > eps):
        n += 1
        _x = x
        if f(a) * f(x) < 0:
            b = x
            x = (a + x) / 2
        elif f(a) * f(x) == 0:
            break
        else:
            a = x
            x = (x + b) / 2
    
    print(f'Root of the equation Lx(x) = 0 is {x} with precision eps = {eps}.')
