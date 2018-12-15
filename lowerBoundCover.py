"""Print numbers for lower bound covering"""
start = int(input("Enter the start value: "))
mod = int(input("Enter the mod: "))
string = ""
for i in range(start,256,mod):
	string= string + str(i) + ", "
print(string)
