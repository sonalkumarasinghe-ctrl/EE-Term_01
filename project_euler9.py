from math import*
val=None
for r in range(1,1000):
    if val==None:
        for s in range(r,1000):
            py=sqrt(r**2+s**2)
            if int(py)==py and py<1000:
                val=r*s*py
                break
    else:
        break        
print(val)        