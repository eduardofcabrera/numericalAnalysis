N0 = 100

def sgn(x):

    if x < 0: return -1
    elif x == 0: return 0
    else: return 1

def findZeroInterval(start, f, interval):

    p = start
    f_in = f(start)
    count = 0
    if f_in == 0:
        return [start-1, start+interval-1]

    while count < N0:
        p_ = p + interval
        fp_ = f(p_)

        if sgn(f_in)*sgn(fp_) == -1:
            return [p, p_]

        if fp_ == 0:
            return [p+1, p_+1]

        p += interval
        count += 1
    
    return "Falhou"


def main():

    pass

main()