"""Try c(n,2) with the new formula"""

import math

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
    return int(n != 0 and ((n & (n - 1)) == 0))

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

def _crToo(n):
    if n%4 == 0 and n > 4:
        return 2 * _m(n)[0] - 2 - 3 * _delta(n)
    else:
        return 0

def _crThree(n):
    if n%4 == 1:
        return 2 * _m(n)[0] - 2 - 2 * _delta(n-1)
    else:
        return 0

def _cdThree(n):
    if n < 5:
        return 0
    else:
        return 2 * (math.floor(math.log(n-1,2))-1)

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

def _cdThreeCue(n):
    #!!!
    if n < 13:
        return 0
    else:
        return 2*_e(n)

def _cdTwo(n):
    #!!!
    if n < 6:
        return 0
    else:
        return 2*_x(n)

def _ca(n):
    if n < 7 or n%4 == 1 or n%4 == 2:
        return 0
    else:
        return 2

def _cThree(n):
    return _cp(n) + _crToo(n) + _crThree(n) + _cdThree(n) + _cdThreeCue(n) + _cdTwo(n) + _ca(n)

def main():
    verts = int(input("Enter the number of vertices >= 4: "))
    print("cp("+str(verts)+",3)",_cp(verts))
    print("cr2("+str(verts)+")",_crToo(verts))
    print("cr3("+str(verts)+")",_crThree(verts))
    print("cd3("+str(verts)+")",_cdThree(verts))
    print("cd3q("+str(verts)+")",_cdThreeCue(verts))
    print("cd2("+str(verts)+")",_cdTwo(verts))
    print("ca("+str(verts)+",3)",_ca(verts))
    print("c("+str(verts)+",3)",_cThree(verts))
##    for verts in range(4,289):
##        print("c("+str(verts)+",3)",_cThree(verts))

if __name__ == "__main__":
    main()
