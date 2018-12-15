"""
Creates a list of all n-digit binary numbers, where n = vertices - 1. Does not include "mirrors."
"""
def binaryGenerator(verts):
    listOfBinaries = []
    digitLength = verts - 1
    for x in range(2**(digitLength)):
        string = ("{:0%db}"%digitLength).format(x)
        if not string in listOfBinaries and not string[::-1] in listOfBinaries:
                listOfBinaries.append(string)
    return listOfBinaries

def onesAmountFilter(listOfBinaries, onesAmount):
    filteredList = []
    for string in listOfBinaries:
        if string.count("1") == onesAmount:
            filteredList.append(string)
    return filteredList

def main():
    verts = int(input("Enter the number of vertices: "))
    queryOnes = input("Enter the number of ones in each sting, or enter N to get all strings: ")
    if queryOnes == "N":
        print("Vertices =", verts)
        for string in binaryGenerator(verts):
            print(string)
    else:
        onesAmount = int(queryOnes)
        if onesAmount > verts - 1:
            print("ERROR")
        else:
            print("Vertices =", verts)
            for string in onesAmountFilter(binaryGenerator(verts), onesAmount):
                print(string)
if __name__ == "__main__":
    main()
