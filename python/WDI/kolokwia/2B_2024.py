def A(n):
    i = 1
    sume = 0
    while i < n:
        if n%i == 0:
            sume += i
        i += 1
    return sume

def B(n):
    a = 0
    b = 1

    while b < n:
        a, b = b, a + b

    if b == n:
        return a + b
    
    return b

def C(n):
    tmp = n
    result = 0
    while tmp != 0:
        result *= 10
        result += tmp%10
        tmp //= 10
    return result + n


def cycle(x, n):
    result = x
    def rek(x, n, c = 0, s = ""):
        nonlocal result
        if c == n:
            return float("inf")
        if c != 0 and result == x:
            print(s)
            return c
        
        return min(rek(A(x), n, c + 1, s + "A"), min(rek(B(x), n, c + 1, s + "B"), rek(C(x), n, c + 1,  s + "C")))

    h = rek(x, n)

    if h < n:
        return h
    else:
        return 0

print(cycle(29, 6))
