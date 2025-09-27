from math import*
def is_prime(num):
    a=True
    if num==1:
        return False
    for r in range(2,int(sqrt(num)+1)):
        if num%r==0   and num!=2 :
            return False
    else:
        return a  
prime,i,count=[2],3,1    
while count<=6:
    if is_prime(i)==True:
        prime.append(i)
        i+=2
        count+=1
print(prime)        



