# Starts at zero

for x in range(0,16):
    n = 2 + 4 *(2**(x+3)+(-1)**x-3)/3
    c = 5 + 57 * (x + 1) + 26 * ((x + 1)%2) + 25 * (2**(2+x)-(-1)**(x)-6*x-9)/3
    print(x)
    print("n(x) =",n)
    print("c(n(x)) =",c)
    print()

for x in range(0,8):
    print((2/3)*(4**(x+2)-1))
    print((1/3)*(4**(x+3)-10))
