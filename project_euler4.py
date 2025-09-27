def palindrome(num):
    if str(num)==str(num)[::-1]:
        return True
vals=[]    
for r in range(999,99,-1):
    for s in range(r+1,99,-1):
        if palindrome(r*s)==True:
            vals.append(r*s)
print(max(vals))             

# Answer is 906609