from math import*
def is_prime(num):
    a=True
    for r in range(2,int(sqrt(num)+1)):
        if num%r==0 and num!=2:
            return False
    else:
        return a    
num=int(input("Enter the Val-:"))
k = num
i = 3
while is_prime(k)==False:
        if k % i == 0:
                k //= i
        i +=2
print(k)    #Answer is 6857    