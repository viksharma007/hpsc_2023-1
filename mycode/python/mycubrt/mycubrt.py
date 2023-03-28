"""
A python module for calculating square root using the 
Newton's method implemented in ME522 class
"""

def sqrtNT(x,debug=False,specialCases=True):
	"""
	The actual sqrtNT function
	Inputs
	x: the number whose square root is to be calculated
	debug: True if iteration details need to be printed. Default value is False
	specialCases: False to disable zero and negative number check. Default value is True

	"""
	from numpy import nan
	
	if specialCases:
		if x==0.:
			return 0.
		elif x<0.:
			print("An error has occured since you have passed a negative value for"
				"x which does not have a real square root")
			return nan
	assert x>0., "Input not recognised"	
	s=1.
	kmax=100
	tol=1.0e-14
	for k in range(kmax):
		if debug:
			print("At iteration number %s, s= %20.15f" %(k,s))
		s0=s
		s = (2*s + (x/(s*s)))/3
		delta_s=s-s0
		if(abs(delta_s/x))<tol:
			break
	if debug:
		print("After %s iterations,  s=%20.15f" %(k+1,s))
	return s
