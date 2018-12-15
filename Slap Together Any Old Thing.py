"Just slap some shit together"
import dymacekTheoremVersionTwo
import math

importantNumbers = [10,18,42,82,170,338,682,1362,2730,5458,10922,21842]

for i in range(234,240):
    for n in range(-10,10):
        for num in importantNumbers:   
            lower = math.ceil(7*math.log(3*num + n,2) + (25*num - i)/8)
            check = dymacekTheoremVersionTwo._c(num) - lower
            if check != 0:
                print("NO, NO, NO, NO, NO")
            else:
                print(str(n)+", "+str(i)+", "+str(num))
                print(check)
        print("\n\nXXX\n\n")
