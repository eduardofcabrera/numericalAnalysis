import math

TOL = 10e-8
N0 = 1000

def derivate(p, f):
    
    fp = f(p)
    fp_ = f(p + TOL)
    deltaP = TOL
    
    return (fp_ - fp) / deltaP

def newtonMethod(p0, f):
    
    for i in range(N0):
        fp = f(p0)
        f_ = derivate(p0, f)
        
        p = p0 - fp/f_
        
        if abs(p - p0) < TOL:
            return p

        p0 = p
        
    return "Falhou"

print(newtonMethod(-1.2, lambda x: math.sin(x) - x))
        
    
    

    

    

