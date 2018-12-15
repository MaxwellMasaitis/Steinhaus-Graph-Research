"""Try c(n,3)"""

import math

def _m(n):
    """
    _m(n) is the set of numbers m, q, r number such that n = (2**m) * (2 * q + 1) + r
    0 <= r < 4, m >= 2, q >= 0
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

def _e(n):
    """
    _e(n) is the number of 1s in the binary expansion of n-1, omitting the first digit from the left and a number of digits on the right.
    The number removed from the right is either 2, or the index of the first 0 from the right of the string, whichever is largest.
    """
    digitLength = n - 1
    string = str(bin(digitLength))[2:]
    index = string.rfind("0")
    index = len(string) - 1 - index
    j = max(2, index)
    string = string[1:-j]
    return string.count('1')

def _x(n):
    """
    _x(n) is the number of 1s in the binary expansion of n-2, omitting a number of digits on the right.
    The number removed from the right is either 2, or the index of the first 0 from the right of the string, whichever is largest.
    """
    digitLength = n - 2
    string = str(bin(digitLength))[2:]
    index = string.rfind("0")
    index = len(string) - 1 - index
    k = max(2, index)
    string = string[:-k]
    return string.count('1')

def _mu(n):
    """
    _mu(n) is the floor of lg(n-2), with 1 subtracted from it
    """
    return math.floor(math.log(n-2,2))-1

def _cp(n):
    """
    A selection of paths
    """
    if n-2 >= 2**(_mu(n)+1) and n-2 < 3*2**_mu(n):
        return n - 1 - 2**(_mu(n)+1)
    elif 3*2**_mu(n) <= n-2 and n-2 < 2**(_mu(n)+2)-1:
        return 2**(_mu(n)+2) + 1 - n
    elif int((n-1) != 0 and (((n-1) & ((n-1) - 1)) == 0)) == 1:
        return 0

def _delta(n):
    """
    _delta(n) is 0 unless n > 5 and n is a power of 2
    """
    if n <= 5:
        return 0
    else:
        return int(n != 0 and ((n & (n - 1)) == 0))

def _cThree(n):
    """
    The number of strings of n vertices that contain exactly 3 1s
    """
    if n >= 8 and n%4 == 0:
        s = 2*_m(n)[0] - 3*_delta(n)
    elif n >= 9 and n%4 == 1:
        s = 2*(_m(n)[0]-1-_delta(n-1))
    elif n%4 == 3:
        s = 2
    else:
        s = 0
    return _cp(n) + 2 * (math.floor(math.log(n-1,2))+_x(n)+_e(n)-1) + s

def main():
##    verts = int(input("Enter the number of vertices >= 4: "))
##    print(_cp(verts))
##    print("c("+str(verts)+",3)",_cThree(verts))
    for verts in range(4,289):
        print("c("+str(verts)+",3)",_cThree(verts))
##        print("cp("+str(verts)+",3)",_cp(verts))

if __name__ == "__main__":
    main()
