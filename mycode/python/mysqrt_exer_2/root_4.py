from mysqrt import *
import sys
#with open("square_root_value.txt","r") as f:
#	a = f.read()
#a = int(a)


root_val = sys.argv[1]

print(root_val)

a = int(root_val[5])
print(f"Number = {a}")

x = sqrtNT(a)

print (f"value of square root of {a} is = {x}")
