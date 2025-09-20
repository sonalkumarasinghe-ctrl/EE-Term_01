## Given x (int) print a christmas tree of height x
def christmas_tree(x):
    for r in range(0,x):
        print(" " * (x - r - 1) + "*" * (2 * r + 1))
      
 ## x0 = "apple", y0 = "adcsjncjsppaxjjnaxle" --> True if all characters of x0 are in y0 in order, y0 = "bsdpple" --> False, y0 = "paple" --> False
def detector(x0,y0):
    extractor=''
    for letter in y0:
        if letter in x0:extractor+=letter
    if extractor==x0:
        print('True')
    else:
        print('False')              