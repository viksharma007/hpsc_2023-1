import timeit

def myCubrt(x,debug=False):
    if x == 0:
        return 0
    s = 1
    kmax = 100
    tol = 1e-14
    for i in range(kmax):
        if debug:
            print(f"The value at iteration {i}")
        s_0 = s
        s = (2*s + x/(s*s))/3
        delta_s = (s -s_0)
        if (abs(delta_s/x)) < tol:
            break
        iter = i
        result = timeit.timeit('myCubrt',globals=globals(),number = iter)
        print(result)
        if debug:
            print(f"The value of cube root of {x} is {s}")
    return s


    
def test_main():
    import numpy as np
    cube_test = [8,-27,64,-256]
    for x in cube_test:
        s = myCubrt(x)
        s_num = np.cbrt(x)
        print("The test of f{x}")
        print(f"The value of cube root function = {s} and the value of the s_num = {s_num}")
        assert abs(s - s_num) < 1e-14, "Your value is not converged to required value"
