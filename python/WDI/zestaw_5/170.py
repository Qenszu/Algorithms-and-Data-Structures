
def f(a,b):
    if a==0: return b+1
    if b==0: return f(a-1,1)
    return f(a-1,f(a,b-1))


print(f(2,3))
