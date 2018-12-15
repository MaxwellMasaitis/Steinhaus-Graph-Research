"""Try c(n,4) with the new formula"""

import math

def _mu(n):
    """
    _mu(n) is the floor of lg((n-2)/3)
    """
    return math.floor(math.log((n-2)/3,2))

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

def _ca(n):
    if n > 5:
        return 1
    else:
        return 0

def _cfTwoTwo(n):
    if n -1 > 4 and (n - 1) != 0 and (((n - 1) & ((n - 1) - 1)) == 0):
        return 1
    else:
        return 0

def _delta(n):
    """
    _delta(n) is 0 unless n is a power of 2
    """
    return int(n != 0 and ((n & (n - 1)) == 0))

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

def _cfThreeThree(n):
    if n >= 7 and n%4 == 3:
        return 2 * (_m(n+1)[0] - 1) - 3 * _delta(n+1)
    else:
        return 0

def _cfTwoThree(n):
    if n > 7 and n%4 ==0:
        return 2*(_m(n)[0] -1 - _delta(n))
    else:
        return 0

def _cFour(n):
    return _cp(n) + _ca(n) + _cfTwoTwo(n) + _cfThreeThree(n) + _cfTwoThree(n)

def main():
    verts = int(input("Enter the number of vertices >= 5: "))
    print("cp("+str(verts)+",4)",_cp(verts))
    print("ca("+str(verts)+")",_ca(verts))
    print("cf22("+str(verts)+")",_cfTwoTwo(verts))
    print("cf33("+str(verts)+")",_cfThreeThree(verts))
    print("cf23("+str(verts)+")",_cfTwoThree(verts))
    print("c("+str(verts)+",4)",_cFour(verts))
##    for verts in range(5,289):
##        print("c("+str(verts)+",4)",_cFour(verts))

if __name__ == "__main__":
    main()
