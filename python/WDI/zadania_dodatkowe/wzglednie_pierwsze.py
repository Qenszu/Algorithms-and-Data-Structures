def euklides(a, b):
    while b != 0:
        a, b = b , a%b
    
    return a

def wzglednie_pierwsze(a , b):
    if euklides(a, b) == 1:
        return True
    return False

print(wzglednie_pierwsze(7, 9))