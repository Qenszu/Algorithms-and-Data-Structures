"""Każdy klocek to przedział w postaci [a,b]. Dany jest ciąg klocków [a1, b1], [a2, b2], ..., [an, bn]. Klocki spadają
   na oś liczbową w podanej kolejności w ciągu. Z danego ciągu klocków możemy usunąć dowolne klocki. Proszę napisać funkcję 
   klocki(T), która oblicza, jaką najwyższa wieża może powstać, tak aby każdy kolejny spadający klocek mieścił się w całości
   w tym, który spadł tuż przed nim"""


def klocki(T):
    result = 0
    size = len(T)


    def rek(T, size, ind = 0, length = 0):
        nonlocal result 
        if ind + 1 == size:
            result = max(result, length)
            return 
        
        if T[ind][0] <= T[ind+1][0] and T[ind][1] >= T[ind+1][1]:
            rek(T, size, ind + 1, length + 1)
        
        rek(T, size, ind+1, length)

    
    rek(T, size)
    return result + 1

T = [(1,6), (2,3), (2,5)]

print(klocki(T))        