from zad7testy import runtests

def maze(L):
    return 0

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = False )

L = [   "....",
        "..#.",
        "..#.",
        "...." ]
print(maze(L))