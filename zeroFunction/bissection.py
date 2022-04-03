import math

TOL = 10e-8;
N0 = 1000;

def is_precision(fp):

    if abs(fp) < TOL:
        return True
    return False

def sgn(x):

    if x < 0: return -1
    elif x == 0: return 0
    else: return 1

def bissection(f, a, b):

    fa = f(a)

    for _ in range(0, N0):
        p = a + (b - a) / 2
        fp = f(p)

        if fp == 0 or is_precision(fp):
            return round(p, 8)
        if sgn(fa)*sgn(fp) > 0:
            a = p
            fa = fp
        else: b = p

    return "Falhou"

def function(x):
    return math.sqrt(x) - math.cos(x)

def main():

    a = -4
    b = -2

    result = bissection(lambda x: x + 1, a, b)
    return result

if __name__ == '__main__':
    main() 
