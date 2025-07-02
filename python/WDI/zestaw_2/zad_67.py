from math import sqrt
end = None
def czy_pierwsza(x):
    if x == 2:
        return True
    for i in range(2, int(sqrt(x) + 1)):
        if x%i == 0:
            return False
    return True
    end

tab = [6, 9, 10, 3, 5, 12, 2, 11, 12, 2131]
size = len(tab)
T = [False for a in range(size)]

def jump(tab, index, T):
    size = len(tab)
    for i in range(2, tab[index]+1):
        if tab[index]%i == 0 and czy_pierwsza(i):
                if index + i > size-1:
                     break
                else: 
                    T[index + i] = True
                    jump(tab, index+i, T)
    end


jump(tab, 0, T)
if T[size-1]:
     print("Da sie")
else:
     print("Nie da sie")
