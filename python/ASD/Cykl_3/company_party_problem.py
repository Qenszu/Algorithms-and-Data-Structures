class Emp:
    def __init__(self, fun):
        self.emp = []
        self.fun = fun
        self.f = -1
        self.g = -1

def f(v):
    if v.f != -1:
        return v.f
    f1 = v.fun
    for u in v.emp:
        f1 += g(u)
    f2 = g(v)

    v.f = max(f1, f2)
    return v.f

def g(v):
    if v.g != -1:
        return v.g
    
    v.g = 0
    
    for u in v.emp:
        v.g += f(u)

    return v.g

