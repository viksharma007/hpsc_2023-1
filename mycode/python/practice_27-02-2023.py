import pdb
x = 'three'
y = 22.0

def f(z):
	pdb.set_trace() 
	x = z + 10
	print(f"inside th function f: after th eexecution of assign statement x={x}, y={y},z={z}")
	return x
	
y = f(x)

print("after calling function the values are")
print(f"x = {x}")
print(f"y = {y}")
