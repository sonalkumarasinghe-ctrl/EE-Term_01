from math import*
def is_prime(num):
    a=True
    for r in range(2,int(sqrt(num)+1)):
        if num%r==0 or num!=2:
            return False
    else:
        return a    
num=int(input("Enter the Val-:"))
Result=is_prime(num)
for r in range(num,2,-1):
    
    

            
        