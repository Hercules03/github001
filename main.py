print("Please Enter Your name: ")
name = input()
print("Hello " + name)

import math
def get_roots(a,b,c):
    d=b**2-4*a*c
    if a==0:
        if b==0:
            if c==0:
                print('1')
            else:
                print('2')