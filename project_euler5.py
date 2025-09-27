from math import*
divider=[r for r in range(2,21)]
num,con=20,False
while con==False:
    for r in divider:
        if num%r!=0:
            num+=20
            break
    else:
        print(num)
        con=True

#answer=232792560       