"""Find various values to help prove the bounds of c3q(n)"""
import math
import CN2v2
import dymacekTheoremVersionTwo

print("{0:>5}{1:>7}{2:>10}{3:>8}{4:>5}{5:>5}{6:>16}{7:>7}".format("n","c3q(n)","(n-21)/8","ceiling","u'n","d'n","binary","cap"))
for n in range(13,5501):
    q = CN2v2._cq(n)
    c = math.ceil((n-21)/8)
##    if q == c:
##        print("{0:5}{1:7}{2:10}{3:8}{4:5}{5:5}{6:>16}{7:7}".format(n,q,(n-21)/8,c,dymacekTheoremVersionTwo._u(n),dymacekTheoremVersionTwo._d(n),bin(n)[2:],n-8*q))
    print("{0:5}{1:7}{2:10}{3:8}{4:5}{5:5}{6:>16}{7:7}".format(n,q,(n-21)/8,c,dymacekTheoremVersionTwo._u(n),dymacekTheoremVersionTwo._d(n),bin(n)[2:],n-8*q))

##for l in range(3,8):
##    n = int((4**l+2)/3)
##    for increment in range(-9,5):
##        q = CN2v2._cq(n+increment)
##        c = math.ceil((n+increment-21)/8)
##        print("{0:5}{1:7}{2:10}{3:8}{4:5}{5:5}{6:>16}{7:7}".format(n+increment,q,(n+increment-21)/8,c,dymacekTheoremVersionTwo._u(n+increment),dymacekTheoremVersionTwo._d(n+increment),bin(n+increment)[2:],n+increment-8*q))


##n = int(input("Enter an n: "))
##q = CN2v2._cq(n)
##c = math.ceil((n-21)/8)
##print("{0:>5}{1:>7}{2:>10}{3:>8}".format("n","c3q(n)","(n-21)/8","ceiling"))
##print("{0:5}{1:7}{2:10}{3:8}".format(n,q,(n-21)/8,c))
