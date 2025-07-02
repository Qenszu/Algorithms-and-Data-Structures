def multi(T):
    naj = 0
    for s in range(len(T)):
        if czy_powtarza(s):
            naj = max(naj, len(s))
    return naj

def czy_powtarza(s):
    for i in range(1, len(s)//2+1):
        if len(s) % i == 0:
            podciag = s[:i]
            if podciag * (len(s) // i) == s:
                return True
    return False


    
tab = ["ABCABCABC", "AAAA", "ASDQFAF"]

print(multi(tab))
            