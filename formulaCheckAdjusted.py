"""Remove various parts"""

import math
import CN2v2
import CN3v2
import CN4v2
import CPGeneric

def _c(n):
    if n < 6:
        # NOT DONE
        if n == 1:
            return 1
        elif n == 2:
            return n
        elif n == 3:
            return n + CN2v2._cTwo(n)
        elif n == 4:
            return n + CN2v2._cTwo(n) + CN3v2._cThree(n)
        elif n == 5:
            return n + CN2v2._cTwo(n) + CN3v2._cThree(n) + CN4v2._cFour(n)
    elif n >= 6:
        genericSum = 0
        for item in range(5, n):
            genericSum += CPGeneric._cp(n,item)
        return (n + CN2v2._cTwo(n) + CN3v2._cThree(n) + CN4v2._cFour(n) + genericSum) - ((n-2)+1+(n-1)+(n-2)+1+CN2v2._cq(n))

def main():
##    verts = int(input("Enter the number of vertices >= 1: "))
##    print("c("+str(verts)+")",_c(verts))
    for verts in range(6,289):
        print("c("+str(verts)+")",_c(verts))

if __name__ == "__main__":
    main()
