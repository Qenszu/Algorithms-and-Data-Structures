""""Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe
odważenie określonej masy. Odważniki można umieszczać tylko na jednej szalc"""

T = [1, 3, 5, 7, 10, 24]

def rek(T, w, i = 0):
    size = len(T)
    
    if w == 0 or w-T[i]:
        return True
    if w < 0 or i == size:
        return False
    if rek(T, w-T[i], i+1):
         print(T[i])
         return True
    elif rek(T, w, i+1):
         print(T[i])
         return True
    

print(rek(T, 25))
    
    
    

    