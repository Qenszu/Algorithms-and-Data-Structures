"""Dwie osoby otrzymały ten sam ciąg liter. Każda osoba pocięła go na kawałki i pomieszała.
Proszę napisać program, który otrzymując dwa zbiory kawałków odtwarza napis początkowy jeżeli 
odtworzenie to jest jednoznaczne lub stwierdza brak możliwości jednoznacznego odtworzenia napisu. Na przykład
dla zbiorów (1) ab,cde,cfed,fab (2) abc,abc,def,fed odtworzony napis to: abcdefabcfed"""

def all_0(T):
    size = len(T)

    for i in range(size):
        if T[i] != 0:
            return False
        
    return True
    

def func(T1, T2, s1="", s2="", i1=0, i2=0):
    # Base case: If both lists are fully processed
    if all_0(T1) and all_0(T2):
        if s1 == s2:
            return s1  # Successful reconstruction
        else:
            return None  # Mismatch, no valid reconstruction

    # Try using elements from T2
    for j in range(len(T2)):
        if T2[j] != 0:
            Tz2 = T2.copy()
            Tz2[j] = 0
            result = func(T1, Tz2, s1, s2 + T2[j], i1, i2 + 1)
            if result:  # If a valid result is found, return it
                return result

    # Try using elements from T1
    for i in range(len(T1)):
        if T1[i] != 0:
            Tz1 = T1.copy()
            Tz1[i] = 0
            result = func(Tz1, T2, s1 + T1[i], s2, i1 + 1, i2)
            if result:  # If a valid result is found, return it
                return result

    # If no valid reconstruction is possible
    return None


# Example usage
T1 = ["ab", "cde", "cfed", "fab"]
T2 = ["abc", "abc", "def", "fed"]

result = func(T1, T2)
if result:
    print(result)
else:
    print("Brak odzorowania")

