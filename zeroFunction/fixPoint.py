import math

TOL = 10e-8
N0 = 1000

def is_precision(p, p0):

    if abs(p - p0) < TOL:
        return True
    return False

def fixPoint(g, p0):

    for _ in range(0, N0):
        p = g(p0)
        if is_precision(p, p0):
            return round(p, 5)
        p0 = p
    return "Falhou"

def main():

    pass

if __name__ == "__main__":
    main()