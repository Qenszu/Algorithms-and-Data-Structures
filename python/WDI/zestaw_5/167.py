""""Dane jest słowo składające się z liter alfabetu angielskiego. Słowo to tniemy na co najmniej
dwa kawałki, tak aby każdy kawałek zawierał dokładnie jedną samogłoskę. Proszę napisać funkcję, która
zwraca liczbę sposobów pocięcia słowa na kawałki."""

def pozycja_nastepnej_samogloski(s, start = 0):
    for i in range(start, len(s)):
        if s[i] in {'a', 'e', 'i', 'o', 'u'}:
            return i
    return -1

def liczba_pociec(s, start = 0):

    if start == 0:
        p1 = pozycja_nastepnej_samogloski(s, start)
        if p1 < 0:
            return 0
        
        p2 = pozycja_nastepnej_samogloski(s, p1+1)
        if p2 < 0:
            return 0
        return (p2-p1)*liczba_pociec(s, p2)
    #end if

    else:
        p = pozycja_nastepnej_samogloski(s, start+1)
        if p < 0:
            return 1
        
        return (p-start)*liczba_pociec(s,p)


print(liczba_pociec("hello"))
