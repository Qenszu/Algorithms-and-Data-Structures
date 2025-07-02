"""Problem 8 Hetmanów"""

kolum = [0 in range(8)]
przekatna1 = [0 in range(15)]
przekatna2 = [0 in range(15)]
wynik = [(0,0) in range(8)]

def rek(kolum, przekatna1, przekatna2, wynik, i = 0):
    if i == 8:
        return True
    
    for j in range(8):
        if kolum[j] == 0 and przekatna1[i+j] == 0 and przekatna2[7-j+i] == 0:
            wynik[i] = (i, j)
            kolum[j] = 1
            przekatna1[j] = 1
            przekatna2[j] = 1
            if rek(kolum, przekatna1, przekatna2, wynik, i + 1):
                return True
            else:
                wynik[i] = (0, 0)
                kolum[j] = 0
                przekatna1[j] = 0
                przekatna2[j] = 0


rek(kolum, przekatna1, przekatna2, wynik)
print(wynik)
