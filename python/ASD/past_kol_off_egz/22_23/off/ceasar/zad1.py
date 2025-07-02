def ceasar(s):
    # Wstawiamy znaki separatora '#' między literami, aby obsługiwać tylko palindromy o nieparzystej długości
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    P = [0] * n  # Tablica promieni palindromów
    C = 0  # Środek aktualnego najdłuższego palindromu
    R = 0  # Prawa granica aktualnego najdłuższego palindromu
    
    for i in range(n):
        print("i: ", i)
        mirr = 2 * C - i  # Odbicie punktu i względem C
        print("mirr: ", mirr)
        if i < R:
            P[i] = min(R - i, P[mirr])  # Możemy skopiować część wartości z symetrycznego punktu
            print("P: ", P)
        
        # Próba rozszerzenia palindromu wokół i
        while i - P[i] - 1 >= 0 and i + P[i] + 1 < n and t[i - P[i] - 1] == t[i + P[i] + 1]:
            P[i] += 1
            print("P2: ", P)
        
        # Jeśli nowy palindrom wychodzi poza R, aktualizujemy C i R
        if i + P[i] > R:
            C = i
            R = i + P[i]
            print("C i R: ", C," ", R)
    
    # Znalezienie maksymalnej długości palindromu o nieparzystej długości (bez separatorów '#')
    max_length = 0
    for i in range(n):
        if P[i] % 2 == 1:  # Długość palindromu w oryginalnym napisie jest nieparzysta
            max_length = max(max_length, P[i])
    
    return max_length


s = "tot"
print(ceasar(s))
        

    