"""
Creates a list of all of the n digit binaries that contain only 2 ones, without mirror copies.
Mirror copy: 11000000000000 == 00000000000011
The length of the binary string is = VERTS - 1
The number of zeroes in the string is = stringLength - 2
"""
def binaryStrings(verts):
    maxZeroes = verts - 3
    listOfBinaries = []

    for r in range(0,maxZeroes + 1):
        for s in range(0,maxZeroes + 1 - r):
            t = maxZeroes - r - s
            string = r * '0' + '1' + s * '0' + '1' + t * '0'
            if not string in listOfBinaries and not string[::-1] in listOfBinaries:
                listOfBinaries.append(string)

    return listOfBinaries

def main():
    verts = int(input("Enter the number of vertices: "))
    print("Vertices =", verts)
    for string in binaryStrings(verts):
        print(string)

if __name__ == "__main__":
    main()
