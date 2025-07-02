
j = 1       
silnia = 1
w = 1
cos = 1

for n in range(1, 100):
    j = j * (-1)
    silnia *= (2*n - 1)*(2*n)
    w *= x*x    
    cos += (j/silnia)*w
