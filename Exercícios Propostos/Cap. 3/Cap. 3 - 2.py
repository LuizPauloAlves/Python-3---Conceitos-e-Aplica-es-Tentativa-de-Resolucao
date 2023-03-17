A, B, C = 10, 15, 4
print("1 ", A<B and A<C)   #False
A, B, C = 10, 15, 4
print("2 ", A<B or A<C)   #True
A, B, C = 1, 9, 0
print("3 ", A>=0 and B==C )   #False
A, B, C = 1, 9, 9
print("4 ", A>=0 and B==C)   #True
A, B, C = 1, 9, 0
print("5 ", A>=0 or B==C)   #True
A, B, C = 1, 9, 9
print("6 ", A>=0 or B==C)   #True
A, B, C = 0, 0, 0
print("7 ", B!=0 and A!=C)   #False
A, B, C = 0, 0, 25
print("8 ", B!=0 and A!=C)   #False
A, B, C = 0, 0, 0
print("9 ", B!=0 or A!=C)   #False
A, B, C = 0, 0, 25
print("10 ", B!=0 or A!=C)   #True