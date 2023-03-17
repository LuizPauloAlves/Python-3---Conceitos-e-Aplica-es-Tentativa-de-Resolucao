A, B, C = 10, 15, 4
print("1 ", A<B and A<C or C!=0)   #True
A, B, C = 10, 15, 4
print("2 ", A<B and (A<C or C!=0))   #True
A, B, C = 1, 9, 0
print("3 ",not(A>=0 and B==C))   #True
A, B, C = 1, 9, 9
print("4 ", not(A>=0 and not (B==C)))   #True
A, B, C = 1, 9, 0
print("5 ", (A>=0 or B==C) and B>A)   #True
A, B, C = -2, 0, 2
print("6 ", not(A<=B) or C>B)   #True
A, B, C = -2, 0, 2
print("7 ", not(A<=0) or C>B)   #True
A, B, C = 0, 1, 0
print("8 ", A==0 and B!=0 and C==0)   #True
A, B, C = 5, 0, 0
print("9 ", A==0 and B!=0 and C==0)   #False
A, B, C = 5, 0, 0
print("10 ", A==0 or B!=0 or C==0)   #True
