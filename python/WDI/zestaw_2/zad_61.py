def te_same_cyfry(l1, l2):
    end = None
    tab = [0 for i in range(0, 10)]
    
    while l1 > 0:
        tab[l1%10] += 1
        tab[l2%10] -= 1
        l1 //= 10
        l2 //= 10
    end
    
    pom = 0
    for j in range(10):
        if tab[j] != 0:
            print("Nie sa")
            pom = 1
            break
        end
    end

    if pom != 1:
        print("Sa")

    
        

te_same_cyfry(1238, 3219)
        





