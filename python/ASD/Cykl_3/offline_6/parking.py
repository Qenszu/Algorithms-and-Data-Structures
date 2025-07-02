from zad6testy import runtests

"""
F[i][j] - minimalny dystans miedzy parkingami do i-tego biurowca z wykorzystaniem do j-tego 
parkingu
W funkcji sprawdzamy minimum tego co byla dla i-tego biurowca z wykorzystanie (j-1)-tego parkingu
oraz z tego gdy przypiszemy i-ty biurowiec do j-tego parkingu
"""

def parking(X,Y):
  n = len(X)
  m = len(Y)
  F = [[float("inf") for _ in range(m)] for _ in range(n)]
  F[0][0] = abs(X[0] - Y[0])

  for j in range(1, m):
    F[0][j] = min(F[0][j-1], abs(X[0] - Y[j]))

  for i in range(1, n):
    for j in range(i, m):
      F[i][j] = min(F[i][j-1], abs(X[i] - Y[j]) + F[i-1][j-1])

  return min(F[n-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True)
