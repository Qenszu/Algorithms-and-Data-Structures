from math import log10

def is_prime(n):
    if n == 2 or n == 3 or n == 5:
        return True
    #end if
    if n < 2 or n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    #end if
    
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        #end if
        i += 6
    #end while

    return True

def is_palindrome(n):
    if n < 10:
        return True
    #end if

    temp = n
    result = 0

    while n != 0:
        result += n % 10
        result *= 10
        n //= 10
    #end while

    if temp == (result//10):
        return True
    #end if
    
    return False

def cut(n):
    l = int(log10(n)) + 1
    result = n % 10**(l - 1)
    result //= 10

    return result

def is_super_prime_pali(n):
    while n > 99:
        if is_palindrome(n) and is_prime(n):
            n = cut(n)
        else:
            return False
        #end if
    #end while
        
    if is_prime(n) and is_palindrome(n):
        return True
    #end if
    
    return False

def main_func(n):
    result = 0

    for i in range(2, n):
        if is_super_prime_pali(i):
            print(i)
            result += 1
        #end if
    #end for

    return result


print(main_func(1000))

