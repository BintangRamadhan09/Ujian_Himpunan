# Genap
a1 = 21
A = set()
for i in range (1,a1):
    if i%2 == 0 :
        A.add(i)
print(A)

# Ganjil
B = set()
for i in range (1,a1):
    if i%2 != 0 :
        B.add(i)
print(B)

# Lebih dari -10
C = set()
c1 = -9
for i in range(c1,0):
    C.add(i)
print(C)

# Bilangan Prima
Num = list(range(21))
D = set(filter(lambda x : x % 11 != 0 or x==11 ,
            filter(lambda x : x % 7 !=0 or x==7,
                filter(lambda x : x % 5 !=0 or x==5,
                    filter(lambda x : x % 3 !=0 or x==3,
                        filter(lambda x : x % 2 != 0 or x==2,
                            filter(lambda x : x > 1,Num )))))))
print(D)

# Bilangan Komposit

E = set(filter(lambda x : x % 2 == 0 or x % 3 == 0,
                        filter(lambda x : x > 3,Num )))
print(E)


# Soal A
print( A | B | C | D | E)

# Soal B
print((A & B) | (D & E))

# Soal C
print((A | B) & (D | E))

# Soal D
print((A | B) - (D | E))

# Soal E
print((A | B | C) - (A & E))