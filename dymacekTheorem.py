"""
Try the claw theorem.
"""

import math

def invert(bitString):
   """Returns the bit string with the bits inverted."""
   invertedString = ''
   for bit in bitString:
      if bit == '1':
         invertedString += '0'
      else:
         invertedString += '1'
   return invertedString

def _l(n):
    """
    _l(n) is the floor of lg(n).
    """
    return math.floor(math.log(n,2))

def _g(n):
    """
    _g(n) is 1 if n is a power of 2 and 0 otherwise.
    """
    return int(n != 0 and ((n & (n - 1)) == 0))

def _m(n):
    """
    _m(n) is the set of numbers m, q, r number such that n = (2**m) * (2 * q + 1) + r
    0 r< 4, m > 1, q >= 0
    """
    m = _l(n)
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
            if m <= 1:
                return "ERROR"
        if n == (2**m) * ((2 * q) + 1) + r:
                return [m, q, r]
    
    

def _u(n):
    """
    _u(n) is the sum of (n - 1) - the ones of (n - 2), starting from the left.
    """
    a = n - 1
    b = n - 2
    mainString = str(bin(b))[2:]
    u = 0

    for i in range(len(mainString) - 2):
        if mainString[i] == "1":
            subString = mainString[:i + 1] + "0" * (len(mainString) - i - 1)
            u = u + (a - int(subString,2))
    return u

def _d(n):
    """
    _d(n) is the sum of the substrings of n - 2 in binary.
    The substrings start with each zero in n - 2 and are inverted before being summed.
    """
    b = n - 2
    d = 0
    mainString = str(bin(b))[2:]
    mainString = mainString[1:]
    for i in range(len(mainString) - 2):
        if mainString[i] == "0":
            subString = invert(mainString[i + 1:])
            d = d + int(subString,2)
    return d

def _w(n):
    """
    _w(n) is the number of 1s in the binary expansion of n-1, omitting the first digit from the left and the last two on the right.
    """
    digitLength = n - 1
    string = str(bin(digitLength))[2:]
    string = string[1:-2]
    return string.count('1')

def _p(n):
    """
    _p(n) is a value that is determined by what the second digit from the left is in a binary n - 2.
    """
    digitLength = n - 2
    string = str(bin(digitLength))[2:]
    if int(string[1]) == 0:
        string = string[2:]
        bValue = int(string, 2)
        p = (2**(_l(digitLength) - 1)) + bValue
    else:
        p = (2**_l(digitLength)) - 1
    return p

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

def _c(n):

    if _m(n)[2] == 0:
        s = (4 * _m(n)[0]) + 1 - (5 * _g(n))
    elif _m(n)[2] == 1:
        s = (2 * _m(n)[0]) - _g(n - 1)
    elif _m(n)[2] == 2:
        s = 1
    elif _m(n)[2] == 3:
        s = (2 * _m(n+1)[0]) + 2 - (3 * _g(n + 1))
    
    return (2 * n) - 5 + (4 * _l(n-1)) + _u(n) + _d(n) + _p(n) + (2 * (_w(n) + _e(n) + _x(n))) + s

def main():
    verts = int(input("Enter the number of vertices >= 10: "))
    print("Vertices =", verts)
    print("l",_l(verts - 1))
    print("u",_u(verts))
    print("d",_d(verts))
    print("p",_p(verts))
    print("w",_w(verts))
    print("e",_e(verts))
    print("x",_x(verts))
    print("m",_m(verts))
    print("g",_g(verts))
    print("c:",_c(verts))
##    print("{0:>5}{1:>10}{2:>6}{3:>6}{4:>6}".format("verts","clawfree","u","d","p"))
##    for i in range(9,289):
##        print("{0:5}{1:10}{2:6}{3:6}{4:6}".format(i,_c(i),_u(i),_d(i),_p(i)))
if __name__ == "__main__":
    main()
