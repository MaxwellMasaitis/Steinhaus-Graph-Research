"""
"""

from fullBinaryGenerator import binaryGenerator
from steinhausTriangleGenerator import steinhausGenerator

def main():
    verts = int(input("Enter the number of vertices: "))
    print("Vertices =", verts)
    print()
    for string in binaryGenerator(verts):
        print("String =",string)
        print(steinhausGenerator(string))
        print()

if __name__ == "__main__":
    main()
