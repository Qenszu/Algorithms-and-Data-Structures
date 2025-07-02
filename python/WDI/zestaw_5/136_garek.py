import time

def skok(T,w,k,i):
    n=len(T)
    dx=(1,2,2,1,-1,-2,-2,-1)
    dy=(-2,-1,1,2,2,1,-1,-2)
    nw,nk=w+dx[i],k+dy[i]
    if 0<=nw<n and 0<=nk<n  and  T[nw][nk]==0 :
        return nw,nk
    return -1,-1


def wypisz(T):
    for i in range(len(T)):
        for j in range (len(T)):
            print(f'{T[i][j]:2d}',end=" ")
        print()
    print()
    time.sleep(0.0001)


def ruch(T,w,k,l=1):
    #wypisz(T)
    T[w][k] = l
    n=len(T)
    if n*n==l:
        wypisz(T)

        #exit()
    else:
        for i in range(8):
            nw,nk=skok(T,w,k,i) # nw - nie wiem, nk - nie kojarze
            if nw!=-1:

                ruch(T,nw,nk,l+1)
                T[nw][nk]=0


x=8
T=[[0 for i in range(x)] for j in range(x)]

ruch(T,0,0)
print(T)