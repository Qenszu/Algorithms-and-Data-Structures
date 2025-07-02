a = int(input("Wprowadz 1 liczbe: "))
b = int(input("Wprowadz 2 liczbe: "))
c = int(input("Wprowadz 3 liczbe: "))
d = int(input("Wprowadz 4 liczbe: "))
end = None

tablica = [a, b, c , d]

#tablica.sort(reverse= True)

czy_krecic = True
maksymalna = 0

while czy_krecic:
    czy_wieksza_od_zera = False

    for i in range(4):
        if tablica[i] != 0:
            tablica[i] -= 1
            czy_wieksza_od_zera = True
    end
    
    if czy_wieksza_od_zera:
        maksymalna += 1
    else:
        czy_krecic = False

    end

print("Element maksymalny jest rowny: ", maksymalna)
    


        




   