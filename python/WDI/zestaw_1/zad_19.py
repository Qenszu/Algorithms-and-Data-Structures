def more_step():
    maxi = 0
    index = 2
    for i in range(3, 10000 + 1):
        a1 = i
        a2 = (a1%2)*(3*a1+1)+(1-a1%2)*a1/2
        eps = 1e-10
        steps = 0
        

        while abs(a2-1) > eps:
            a1 = a2
            a2 = (a1%2)*(3*a1+1)+(1-a1%2)*a1/2
            steps += 1
        
        if steps > maxi:
            maxi = steps
            index = i

    return index
    
print(more_step())