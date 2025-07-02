T = [2,5,7,3,5,2,3,5,7,6,9,15,21,17,19,23,2,6,4,8,3,5,7,1,3,2,]

def sequence(T):
    size = len(T)
    ciag = 3
    a1 = None
    a2 = None
    maxi = 1

    while ciag <= size // 2:  # Najdłuższy ciąg nie może być dłuższy niż połowa długości tablicy
        index = 0
        while index + ciag * 2 <= size:  # ograniczenie z prawej strony
            iloczyn = T[index + ciag] / T[index]
            pom = True
            for i in range(1, ciag):
                if index + ciag + i >= size or T[index + i] * iloczyn != T[index + ciag + i] or iloczyn == 1:
                    pom = False
                    break  # zakończ pętlę for, jeśli warunek nie jest spełniony
            
            if maxi < ciag and pom:
                maxi = ciag
                a1 = index
                a2 = index + ciag - 1

            index += 1
        ciag += 1

    print(a1, a2)

sequence(T)
