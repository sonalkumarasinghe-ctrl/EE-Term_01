a=int(input("Enter Val:-"))
def sum_multiply(num):
    sum=0
    for r in range(2,num):
        if r%3==0 or r%5==0:
            sum+=r
    else:
        return sum
sum=sum_multiply(a)
print(f'Sum is {sum}' )           