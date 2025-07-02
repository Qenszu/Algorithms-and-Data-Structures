def func():
    end = None
    tab = [0 for i in range(10)]

    while True:
        x = int(input("Podaj liczbe: "))

        if x == 0:
            break 

        i = 0
        while True:
            if i == 10:
                break
            if tab[i] == x:
                break
            elif tab[i] < x:
                tab[i], x = x, tab[i]
            i += 1
        end
    end

    print(tab[9])


func()           