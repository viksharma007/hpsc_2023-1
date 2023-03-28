'''
A python module for calculating square root using the Newton's method implemented in ME522.
'''
import sys

print(f"This the name of the program is {sys.argv[0]}")

def sqrtNT(x,debug=False):
    '''
    The actual sqrtNT function
    Takes one input x: the number whose square root is to be calculated. 
    '''
    from numpy import nan
    
    if x==0. :
        return 0.
    elif x<0. :
        print("An error has occured since you have passed a negatice value which does not have real square root")
        return nan
    assert x>0., "Input not recignised"
    s = 1.0
    kmax = 100
    tol = 1.0e-14
    for k in range(kmax):
        if debug: 
            print("At Iteration number %s, s = %20.15f" %(k,s))
        s0=s
        s = 0.5*(s + x/s)
        delta_s = s - s0
        if (abs(delta_s)/x)<tol:
             break
    if debug:
        print("After %s number of iteration ,s = %20.15f" %(k+1,s))
    return s

name = sys.argv[0]
y = int(name[7])
print(y)
#f = open("square_root_value.txt",'r')
#y = f.read()
#y = int(y)
z = sqrtNT(y)
print(z)

def test_main():
    from numpy import sqrt
    xvalues = [0.,2.0,100,1.e6]
    for x in xvalues:
        print("Testing with z=%s" %x)
        s=sqrtNT(x)
        s_numpy=sqrt(x)
        print("sqrtNT s = %20.15e, numpy_s = %20.15e" %(s,s_numpy))
        assert abs(s - s_numpy) < 1e-14, "Your sqrt does not agree with numpy sqrt"
