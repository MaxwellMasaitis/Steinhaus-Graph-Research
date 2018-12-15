"""Generic cp formula"""

import math

def _mu(n,k):
    """
    _mu(n,k) is the floor of lg((n-2)/(k-1))
    """
    return math.floor(math.log((n-2)/(k-1),2))

def _cp(n,k):
    """
    A selection of paths
    """
    if (k-1)*2**_mu(n,k) <= n-2 and n-2 < k*2**_mu(n,k):
        return n - 1 - (k-1)*2**_mu(n,k)
    elif k*2**_mu(n,k) <= n-2 and n-2 < (k+1)*2**_mu(n,k)-1:
        return (k+1)*2**_mu(n,k)+1-n
    else:
        return 0

def main():
##    verts = int(input("Enter the number of vertices: "))
##    k = int(input("Enter the number of 1s: "))
##    print("cp("+str(verts)+","+str(k)+")",_cp(verts,k))
    k = int(input("Enter the number of 1s: "))
    for verts in range(k+1,289):
        print("cp("+str(verts)+","+str(k)+")",_cp(verts,k))

if __name__ == "__main__":
    main()
