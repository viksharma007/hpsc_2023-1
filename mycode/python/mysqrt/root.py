from mysqrt import *

with open("square_root_value.txt","r") as f:
	a = f.read()
a = int(a)

x = sqrtNT(a)

print (f"value of square root of {a} is = {x}")
