from time import sleep

def kierunek(T, d0, d1, w, k): #d --> (1, 0)
    if T[w][k] == " ":
        return d0, d1
    if T[w][k] == "/":
        x = d0
        d0 = d1 * (-1)
        d1 = x * (-1)
        return d0, d1
    if T[w][k] == "\\":
        x = d0
        d0 = d1
        d1 = x
        return d0, d1
    
def napraw(ogrod):
    result = None
    N = len(ogrod)
    def rek(T, N, d, w = 0, k = 0, o = 0):
        nonlocal result
        if w == k == N-1:
            print("Jestem")
            result = T
            return True
        print(w, k)
        print(d)
        sleep(0.01)
        d = kierunek(T, d[0], d[1], w, k)
        if w+d[0]<N and w+d[0]>-1 and k+d[1]<N and k+d[1]>-1:
            if rek(T, N, d, w+d[0], k+d[1]):
                return True
            elif T[w][k] == "/" and o < 2:
                T[w][k] = "\\"
                d = kierunek(T, d[0], d[1], w, k)  
                if rek(T, N, d, w+d[0], k+d[1], o + 1):
                    return True
            elif T[w][k] == "\\" and o < 2:
                T[w][k] = "/"
                d = kierunek(T, d[0], d[1], w, k)
                if rek(T, N, d, w+d[0], k+d[1], o + 1):
                    return True
        return 
    rek(ogrod, N, (1,0))
    for a in range(N):
        print(result[a])

ogrod = [
    [" ", " ", " ", " ", " "],
    [" ", "/", " ", "/", " "],
    [" ", " ", " ", " ", " "],
    ["\\", " ", " ", "/", " "],
    [" ", "/", " ", " ", "\\"],
]

napraw(ogrod)

    




    