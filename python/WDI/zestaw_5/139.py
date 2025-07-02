""""Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie 
    posiada innych czynników niż 2, 3, 5. Jedynka też jest taką liczbą. 
    Proszę napisać funkcję rekurencyjną, wypisującą liczby znajdujące się w 
    przedziale od 1 do N włącznie"""

def func(N):
    cnt = 0
    def rek(N, n = 1):
        nonlocal cnt
        print(n)
        cnt += 1
        if n*2 <= N:
            rek(N, n*2)
        if n*3 <= N and n%2 != 0:
            rek(N, n*3)
        if n*5 <= N and n%2 != 0 and n%3 != 0:
            rek(N, n*5)
        return 
    rek(N) 
    print("Liczba: " ,cnt)

N = int(input("> "))
func(N)


