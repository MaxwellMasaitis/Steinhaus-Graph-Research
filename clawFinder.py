"""
Claw Finder?
"""

# Input the string.
# Loading in only the set of binaries that does not include mirrors.
# So, for an accurate result the count must be adjusted
if string != string[::-1]:
    weight = 2
else:
    weight = 1

if "0111" in string or "1110" in string:
    clawfree = False
elif "00101" in string or "10100" in string:
    clawfree = False
elif "01011" in string or "11010" in string:
    clawfree = False
elif "010011" in string or "110010" in string:
    clawfree = False
elif "0010101" in string or "1010100" in string:
    clawfree = False
