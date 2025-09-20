## Given x (int) print a christmas tree of height x
def christmas_tree(x):
    for r in range(0,x):
        print(" " * (x - r - 1) + "*" * (2 * r + 1))
      

print('Hello World')      
