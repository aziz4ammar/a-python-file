from math import*
e=int (input("donner un chiffre:"))
s=0
while e>0:
    t=e%10
    s=s+t
    e = e//10
print ("la somme est =",s)
