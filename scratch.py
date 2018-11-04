a= int(input ("print koeficient a:"))
b= int(input ("print koeficient b:"))
c= int(input ("print koeficient c:"))

if a!=0:
    d= b**2-(4*a*c)
    print (d)
    if d>=0:
        x1 = (b**2 + d**(1/2)) / 2 * a
        x2 = (b**2 - d**(1/2)) / 2 * a
        print(x1, x2)
    else:
        print("equations has no root")


else:
    print("equations has no root")




