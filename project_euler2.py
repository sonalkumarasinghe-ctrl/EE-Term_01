a=int(input("Enter the limit-:"))
fib_seq=[1,2]
def fib(limit):
    global fib_seq
    end=fib_seq[-1]
    fib_seq.append(fib_seq[-1]+fib_seq[-2])
    if end>limit:
        return fib_seq[0:len(fib_seq)-2]
    else:
        return fib(limit)
fibonacci_=fib(a)
print(sum([i for i in fibonacci_ if i%2==0]))