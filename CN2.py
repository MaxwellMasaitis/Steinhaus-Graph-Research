"""Try c(n,2)"""

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

def _mu(n):
    """
    _mu(n) is the floor of lg(n-2)
    """
    return math.floor(math.log(n-2,2))

def _cp(n):
    """
    A selection of paths
    """
    if n == 3:
        return 0
    elif 2**_mu(n) <= n-2 and n-2 < 3*2**(_mu(n)-1) -1:
        return 2**(_mu(n)-1)
    elif 3*2**(_mu(n)-1) - 1 <= n-2 < 2**(_mu(n)+1):
        return n - 1 - 2**_mu(n)

def _u(n):
    ### ACTUALLY IT'S u'n NOW
    a = n - 1
    b = n - 2
    mainString = str(bin(b))[2:]
    u = 0
    # Added a 1 into the range to skip the leftmost digit
    for i in range(1, len(mainString) - 2):
        if mainString[i] == "1":
            subString = mainString[:i+1] + "0" * (len(mainString) - i - 1)
            u = u + (a - int(subString,2))
    return u

def _d(n):
    ### ACTUALLY IT'S d'n NOW
    b = n - 2
    d = 0
    mainString = str(bin(b))[2:]
    # Exclude the rightmost 2 and try to find a 0 on the right
    index = mainString[:-2].rfind("0")
    # range is index + 1, since just 'index' doesn't include the index itself, dummy
    for i in range(2,index + 1):
        if mainString[i] == "0":
            subString = invert(mainString[i+1:])
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

def _cTwo(n):
    """
    The number of strings of n vertices that contain exactly 2 1s
    """
    if n == 3 or n == 4 or n == 6:
        s = 5
    elif n == 5:
        s = 6
    elif n == 8:
        s = 0
    elif n%4 == 0:
        s = 2
    elif n%4 == 3 or n%4 == 1:
        s = 3
    else:
        s = 4
    return n + 1 + _cp(n) + 2*(math.floor(math.log(n-1,2)) + _w(n)) + _u(n) + _d(n) - s

def main():
    verts = int(input("Enter the number of vertices >= 3: "))
    print(_cp(verts))
    print("c("+str(verts)+",2)",_cTwo(verts))
##    for verts in range(3,289):
##        print("c("+str(verts)+",2)",_cTwo(verts))
####        print("cp("+str(verts)+",2)",_cp(verts))

if __name__ == "__main__":
    main()
