""""Na szachownicy o wymiarach 100 na 100 umieszczamy N hetmanów (N < 100). Położenie
hetmanów jest opisywane przez tablicę dane = [(w1, k1),(w2, k2),(w3, k3), ...(wN , kN )]. 
Proszę napisać funkcję, która odpowiada na pytanie: czy żadne z dwa hetmany się nie szachują? 
Do funkcji należy przekazać położenie hetmanów."""

def czy_szachuje(d1, d2):
    if d1[0] == d2[0] or d1[1] == d2[1]:
        return True
    
    tmp_x1 = d1[0]
    tmp_y1 = d1[1]
    i = 1
    while tmp_x1 + i < 100 and tmp_y1 + i  < 100:
        if tmp_x1 + i == d2[0] and tmp_y1 + i == d2[1]:
            return True
        i += 1

    tmp_x1 = d1[0]
    tmp_y1 = d1[1]
    i = 1
    while tmp_x1 - i > -1 and tmp_y1 - i > -1:
        if tmp_x1 - i == d2[0] and tmp_y1 - i == d2[1]:
            return True
        i += 1
    
    tmp_x1 = d1[0]
    tmp_y1 = d1[1]
    i = 1
    while tmp_x1 - i > -1 and tmp_y1 + i < 100:
        if tmp_x1 - i == d2[0] and tmp_y1 + i == d2[1]:
            return True
        i += 1

    tmp_x1 = d1[0]
    tmp_y1 = d1[1]
    i = 1
    while tmp_x1 + i < 100 and tmp_y1 - i > -1:
        if tmp_x1 + i == d2[0] and tmp_y1 - i == d2[1]:
            return True
        i += 1
    
    return False

def func(dane):
    size = len(dane)
    for i in range(size - 1):
        for j in range(i + 1, size):
            if czy_szachuje(dane[i], dane[j]):
                return False
    
    return True


dane = [
    (1, 1), (2, 3), (3, 5), (4, 7), (5, 9),
    (6, 11), (7, 13), (8, 15), (9, 17), (10, 19),
    (11, 21), (12, 23), (13, 25), (14, 27)
]

print(func(dane))