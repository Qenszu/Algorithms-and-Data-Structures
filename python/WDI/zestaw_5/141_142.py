""" Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza 
    czy jest możliwe odważenie określonej masy. Odważniki można umieszczać na obu szalkach. 
    Niech wypisuje te odwazniki"""

def func(T, mas):
    size = len(T)
    l_odw = ""
    p_odw = ""

    def rek(T, size, masp, strl = "", strp = "", masl = 0, ind = 0):
        nonlocal l_odw, p_odw
        if masp == masl:
            l_odw = strl
            p_odw = strp
        if ind < size:
            rek(T, size, masp + T[ind], strl, strp + ", " + str(T[ind]), masl, ind + 1)  
            rek(T, size, masp, strl + ", " + str(T[ind]), strp, masl  + T[ind], ind + 1) 
            rek(T, size, masp, strl, strp, masl, ind + 1) 

    rek(T, size, mas)
    p_odw += " ," + str(mas)
    print("Lewe odwazniki: " ,l_odw[1:])
    print("Prawe odwazniki: " ,p_odw[2:])
        



T = [1, 3, 5, 7, 10, 24, 1]

func(T, 26)


    


