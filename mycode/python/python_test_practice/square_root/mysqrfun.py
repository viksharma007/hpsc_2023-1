def mysqNT(x,debug=False):
    import numpy as np
    if x == 0.0:
       return 0.0
    elif x<0:
        print ("An error has been a=occured because you have paased negative value of x for which real square root does not exist")
        return np.nan 
    assert x>0.0, "Input not recognized"
    kmax = 100
    s = 1
    tol = 1e-14
    for i in range(kmax):
        if debug:
            print(f"The value of iteration is {i}")
        s_0 = s
        s = 0.5 *(s + x/s)
        delta = abs(s - s_0)
        iter = i
        if ((delta/x) < tol):
            break
    if debug:
        print(f"The value of square root is {s}") 
    return s

import nose
def testmain():
    import numpy as np
    test_val = [0.0,2.0,100.0,11.1]
    for x in test_val:
        print(f"testing with the following values = {x}")
        s = mysqNT(x)
        s_num = np.sqrt(x)
        print(f"The value of mysqNT = {s} and The value of numpy sqrt() =  {s_num})")
        assert abs(s -s_num) < 1e-14, "Your value does not agree with numpy value"
    

