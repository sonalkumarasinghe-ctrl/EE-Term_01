from math import*
def is_prime(num):
    a=True
    for r in range(2,int(sqrt(num)+1)):
        if num%r==0:
            return False
    else:
        return a    
b=is_prime(11) 
print(b)       
            
        