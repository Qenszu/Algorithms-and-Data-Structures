from egz1btesty import runtests

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow

def wideentall( T ):
    # tu prosze wpisac wlasna implementacje

    width = [0]

    def dfs1(A, depth):                                 #sprawdza glebokosc i szerokosc drzewa
        if len(width) < depth + 1:
          width.append(0)
        width[depth] += 1
        A.x = depth

        if A.left:
           dfs1(A.left, depth + 1)
        if A.right:
           dfs1(A.right, depth + 1)

    dfs1(T, 0)
    #print(width)
    max_width = max(width)
    max_depth = 0

    for i in range(len(width) - 1, -1, -1):
        if width[i] == max_width:
           max_depth = i
           break
    
    cuts = 0
    def dfs2(A, max_depth):
        nonlocal cuts
        if A.x == max_depth:
            if A.left is not None:
               A.left = None
               cuts += 1
            if A.right is not None:
               A.right = None
               cuts += 1
            return True
        else:
            if A.left is None and A.right is None:
                return False
            
            preety_left = preety_right = True
            if A.left:
                preety_left = dfs2(A.left, max_depth)
            if A.right:
                preety_right = dfs2(A.right, max_depth)


            if not preety_left and not preety_right:
               return False

            if not preety_left:
                A.left = None
                cuts += 1
            
            if not preety_right:
                A.right = None
                cuts += 1
            

            return True

    dfs2(T, max_depth)
           
    return cuts

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = False )

A = Node()
B = Node()
C = Node()
A.left = B
A.right = C
D = Node()
E = Node()
B.left = D
B.right = E
F = Node()
E.right = F
G = Node()
F.right = G
#print(wideentall(A))