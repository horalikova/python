a=int(input("type a number:"))
if a%2==0:
    print("neni prvocislo1")
else:
    o=int((a**(1/2)))
    i=int(3)
    print(o)
    while i<o:
        if a%i == 0:
            print(" neni prvocislo2")
            i=i+1
        else:
            print("prvocislo3")
            break





