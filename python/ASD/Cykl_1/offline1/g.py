from zad1testy import runtests

""""Patryk Opala
Algorytm wykorzystuje typowy algorytm sortowania szybkiego merge sort
z wyjatkiem dwóch warunków "if" które w jednoznaczny sposób rozstrzygają czy dane słowo zapisać 
w obencnej formie bądź czy należy go odwrócić co pomaga w poźniejszym jednoznacznym posortowaniu

Przykład:
Gdy mamy słowo "pies" oraz "seip" są one równoważe i chcemy aby w posortowanej tablicy występowały jedno za drugim. 
Możemy to osiągnąć stosujac znak porówania ">" i sprawdzić który napis jest "większy". Dzięki temu zawsze gdy napotkamy 
w tablicy napisa "pies" lub "seip" to zostanie on zwrócony w postaci słowa "pies".

Na samym końcu wystarczy przejść po posortowanej tablicy i sprawdzić które słowo wystepuje najwiekszą ilość razy"""

def merge_sort(arr):
    size = len(arr)
    if size > 1:
        left_arr = arr[:size//2]
        right_arr = arr[size//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0 
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):

            #ustalamy w jaki sposób zapisać dane słowo
            if left_arr[i] > left_arr[i][::-1]:
                left_arr[i] = left_arr[i][::-1]
            if right_arr[j] > right_arr[j][::-1]:
                right_arr[j] = right_arr[j][::-1]
            
            #sortowanie
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1                                                        
            k += 1                                                           

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

def g(T):
    merge_sort(T)
    maxi = 1
    cnt = 1

    #szukamy słowa które wystepuje największą ilość razy
    for i in range(len(T)-1):
        if T[i] == T[i+1]:
            cnt += 1
            if cnt > maxi:
                maxi = cnt
        else: 
            cnt = 1
    
    return maxi

runtests(g, all_tests= True)

