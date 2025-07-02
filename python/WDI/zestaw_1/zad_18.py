from math import sqrt, pi
end = None

def func():
    a1 = sqrt(0.5)
    a2 = sqrt(0.5 + 0.5 * a1)
    result = a1*a2
    eps = 1e-10

    while a2 - a1 > eps:
        a1 = a2
        a2 = sqrt(0.5 + 0.5 * a1)
        result *= a2
    end

    return 2.0 / result

print(func(), pi)