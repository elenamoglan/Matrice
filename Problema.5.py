A = [[1 , 3, 6, 7,31], 
     [33, 5, 2,11,66], 
     [54,13,42,21,8], 
     [11,32,45,17,9], 
     [77,83,-6,10,89]]
x=1
for i in A:
    sr=0
    for j in i:
        sr+=j
    print(f'Suma randului {x}: {sr}')
    x+=1
x=1
for j in range(0,len(A[0])):
    sc=0
    for i in range(0,len(A)):    
        sc+=A[i][j]
    print(f'Suma coloanei {x}: {sc}')
    x+=1    
sdp = 0
for i in range(0,len(A)):
    sdp += A[i][i]
sds = 0
for i in range(0,len(A)):
    sds += A[len(A)-i-1][i]
print(f'Suma diagonalei secundare {sds}, suma diagonalei principale {sdp}')