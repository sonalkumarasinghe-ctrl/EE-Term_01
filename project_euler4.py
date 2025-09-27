def palindrome(num):
    if str(num)==str(num)[::-1]:
        return True
vals=[]    
for r in range(999,99,-1):
    if palindrome(r**2)==True:
        vals.append(r**2)
print(palindrome(1002))         
        

    
    