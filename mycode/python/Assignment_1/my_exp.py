def my_exp(x):
	from numpy import nan
	exp = 0
	kmax = 100
	factorial = 1
	tol = ones(x.size)*(1e-14)
	for i in range(0,kmax):
		if(i == 0):
			factorial = 1
		else:
			factorial = factorial*i
		exp_0 = exp
		exp = (x**i)/(factorial) + exp
		i = i + 1
		residual = abs(exp - exp_0)
		#print(type(residual))
		print(residual)
		if (residual.max() < tol):
			break
	# print(f"Exponential value is {exp} which convergened at iteration number {i}")
	print(f"Exponential value are {exp}")
	print(f"Series convergened at iteration number {i}")
	print("done")
