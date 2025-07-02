""""Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, 
która odpowiada na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje 
liczbę pierwszą. Długość każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 
jest to możliwe, a dla ciągu 110100 nie jest możliwe"""

def prime(n):
    if n == 2:
        return True
    if n < 2 or n%2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True


def rek(T, i = 0):
    size = len(T)

    if i == size:
        return True


    multi = 1
    sum = 0
    for j in range(size - 1, i - 1, -1):
        if j == 30:
            break
        sum += T[j]*multi
        if prime(sum):
            if rek(T, i+j+1):
                return True
        multi *= 2

    return False


T = [1, 0, 0, 0, 0, 0]

print(rek(T))