"""Try c(n,4)"""

import math

def _m(n):
    """
    _m(n) is the set of numbers m, q, r number such that n = (2**m) * (2 * q + 1) + r
    0 r< 4, m >= 2, q >= 0
    """
    m = math.floor(math.log(n,2))
    q = 0
    r = 0
    while True:
        if n > (2**m) * ((2 * q) + 1) + r:
            while r < 3:
                r += 1
                if n == (2**m) * ((2 * q) + 1) + r:
                    return [m, q, r]
            r = 0
            q += 1
        elif n < (2**m) * ((2 * q) + 1) + r:
            q = 0
            m -=1
            if m < 2:
                return "ERROR"
        if n == (2**m) * ((2 * q) + 1) + r:
                return [m, q, r]

def _mu(n):
    """
    _mu(n) is the floor of lg((n-2)/3)
    """
    return math.floor(math.log((n-2)/3,2))

def _delta(n):
    """
    _delta(n) is 0 unless n > 5 and n is a power of 2
    """
    if n <= 5:
        return 0
    else:
        return int(n != 0 and ((n & (n - 1)) == 0))

def _cp(n):
    """
    A selection of paths
    """
    if n-2 >= 3*2**_mu(n) and n-2 < 2**(_mu(n)+2):
        return n - 1 - 3*2**_mu(n)
    elif n-2 >= 2**(_mu(n)+2) and n-2 < 5*2**_mu(n)-1:
        return 5*2**_mu(n)+1-n
    else:
        return 0

def _cFour(n):
    """
    The number of strings of n vertices that contain exactly 4 1s
    """
    if n >= 8 and n%4 == 0:
        s = 2 * (_m(n)[0] - 1 - _delta(n))
    elif n >= 7 and n%4 == 3:
        s = 2 * (_m(n+1)[0] - 1) - 3 * _delta(n+1)
    else:
        s = 0
    check = int(n >= 6)
    return check + _cp(n) + _delta(n-1) + s

def main():
##    verts = int(input("Enter the number of vertices >= 5: "))
##    print(_cp(verts))
##    print("c("+str(verts)+",4)",_cFour(verts))
    for verts in range(5,289):
        print("c("+str(verts)+",4)",_cFour(verts))
##        print("cp("+str(verts)+",4)",_cp(verts))

if __name__ == "__main__":
    main()
