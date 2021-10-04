n=int(input('Introduceti numarul de linii a matricei patratice:'))
A=[[int(input()) for i in range(n)] for j in range(n)]
print('Matricea introdusa:')
for i in range(len(A)):
    print(A[i])
s1 = 0
for i in range(0,len(A)):
    s1 += A[i][i]
s2 = 0
for i in range(0,len(A)):
    s2 += A[len(A)-i-1][i]
print(f'Suma componentelor diagonalei secundare este {s2}, iar suma componentelor diagonalei principale este {s1}')
s3=0
for i in A:
    for j in i:
        if A.index(i)<i.index(j):
            s3+=j
print(f'Suma componentelor mai sus de diagonala principală este {s3}')
s4=0
for i in A:
    for j in i:
        if A.index(i)>i.index(j):
            s4+=j
print(f'Suma componentelor mai jos de diagonala principală este {s4}')
s5=0
for i in A:
    for j in i:
        if A.index(i)+i.index(j)<n-1:
            s5+=j
print(f'Suma componentelor mai sus de diagonala secundara este {s5}')
s6=0
for i in A:
    for j in i:
        if A.index(i)+i.index(j)>n-1:
            s6+=j
print(f'Suma componentelor mai jos de diagonala secundara este {s6}')
