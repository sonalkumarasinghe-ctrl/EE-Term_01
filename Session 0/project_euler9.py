from math import*
val=None
con=False
a,b,c=1,1,1
for a in range(1,1000):
    if con==False:
        for b in range(a,1000-a):
            c=1000-a-b
            if c**2==a**2+b**2:
                print(a*b*c)
                con=True
                break
#Answer -: 31875000