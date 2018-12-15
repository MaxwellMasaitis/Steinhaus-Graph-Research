"""
Makes the binary grid from the top string.
"""

def steinhausGenerator(string):
    """
    Creates strings and collects them in mainList.
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
    Returns the strings as a square-ified string of 1s,0s, and *s as appropriate.
    """
    squareString = ""
    for string in range(len(mainList)):
        mainList[string] = (("*" * (len(mainList) - len(mainList[string]))) + "*") + mainList[string]
        squareString = squareString + mainList[string] + "\n"
    # Consider adding the *** line to the trueList, since it may help keep things readable for a claw checker?
    squareString = squareString + "*" + "*" * len(mainList)
    return squareString

def main():
    string = input("Enter a top string: ")
    while string != "N":
        print(steinhausGenerator(string))
        string = input("Enter another top string, or N to quit: ")

if __name__ == "__main__":
    main()
