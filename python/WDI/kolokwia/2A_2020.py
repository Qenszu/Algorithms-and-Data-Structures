""""Dwie liczby są zgodne piątkowo, jeżeli posiadają tyle samo cyfr parzystych w ich reprezentacjach w systemie
pozycyjnym o podstawie 5. Dane są dwie tablice int tab1[MAX1][MAX1], tab2[MAX2][MAX2] (MAX2 > MAX1 > 1).
Proszę napisać funkcję, która sprawdzi, czy możliwe jest takie przyłożenie tab1 do tab2, aby w pokrywającym się
obszarze co najmniej 33% odpowiadających sobie elementów z tab1 i tab2 było zgodnych piątkowo. Uwaga: należy
uwzględnić, że tab1 może tylko częściowo przykrywać tab2 (patrz rysunek), a w sprawdzanym obszarze musi znaleźć
się co najmniej jeden element."""

def is5correct(num1, num2):
    even1 = 0
    even2 = 0

    while num1 != 0:
        if (num1 % 5 ) % 2 == 0:
            even1 += 1
        num1 //= 5
    
    while num2 != 0:
        if (num2 % 5 ) % 2 == 0:
            even2 += 1
        num2 //= 5
        
    return even1 == even2

def func(T1, T2):
    size1 = len(T1)
    size2 = len(T2)

    for i in range(size1):                                              #wiersze mniejszej tablicy 
        for j in range(size1):                                          #kolumny mniejszej tablicy

            for a in range(size2):                                      #wiersze wiekszej tablicy 
                for b in range(size2):                                  #kolumny wiekszej tablicy 
                    x = 1