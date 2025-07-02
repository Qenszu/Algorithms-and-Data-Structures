"""""Korzystając z zależności: (n nad k) = (n-1 nad k-1) + (n-1 nad k) proszę napisać 
funkcję obliczającą wartość symbolu Newtona dla argumentów n"""

def symbol_newtona(n ,k):
    if k == 0 or k == n: return 1

    return symbol_newtona(n-1, k-1) + symbol_newtona(n-1, k)

print(symbol_newtona(4, 2))