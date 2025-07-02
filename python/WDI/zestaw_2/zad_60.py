def system_liczbowy(n, system):
    kod = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
    tab = [0 for i in range(0, 64)]
    i = 0

    while n > 0:
        tab[i] = kod[n%system]
        n //= system
        i += 1

    for j in range(i - 1, -1, -1):
        print(tab[j], end = "")

system_liczbowy(195, 2)


