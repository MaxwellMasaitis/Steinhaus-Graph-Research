"""
Makes the binary grid from the diagonal string.
"""

def steinhausGenerator(string):
    """
    Creates strings as if the diagonal string were the top string, and collects them in mainList.
    """
    mainList = [string]
    stringSize = len(string)
    while stringSize > 1:
        nextList = []
        for i in range(len(string) - 1):
            if string[i] == string[i + 1]:
                nextList.append("0")
            else:
                nextList.append("1")
        nextString = "".join(nextList)
        mainList.append(nextString)
        string = nextString
        stringSize -= 1

    """
    "Diagonalizes" the list of strings, and collects them in trueList.
    """
    count = 0
    trueList = []
    while count < len(mainList[0]):
        newString = ""
        for string in range(len(mainList) - count):
            newString += mainList[string][count]
        trueList.append(newString)
        count += 1

    """
    Returns the diagonalized strings as a square-ified string of 1s,0s, and *s as appropriate.
    """
    squareString = ""
    for string in range(len(trueList)):
        trueList[string] = (("*" * (len(trueList) - len(trueList[string]))) + "*") + trueList[string]
        squareString = squareString + trueList[string] + "\n"
    # Consider adding the *** line to the trueList, since it may help keep things readable for a claw checker?
    squareString = squareString + "*" + "*" * len(trueList)
    return squareString

def main():
    string = input("Enter a diagonal string: ")
    while string != "N":
        print(steinhausGenerator(string))
        string = input("Enter another diagonal string, or N to quit: ")

if __name__ == "__main__":
    main()
