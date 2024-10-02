import math  
# Takes variables A and B as 2 sides of an r triangle
# compute A and B to find C 
# print C
def main():
#TO DO
    print("Provide lengths A and B as")
    print("Measurements for a right angled triangle")
    A = input("Enter length A: ")
    B = input("Enter length B: ")
    # input() functions naturally take variables as str()
    Chyp = pythag(A,B)
    print(f"The result for hypotenuse (C) was: {repr(Chyp)}")
    # function repr() used to convert the number to str()
def pythag(A,B):
# Calculates C using sqrt
    Csquare = (int(A)**2 + int(B)**2)
    # int() converts the str()s 
    C = round(math.sqrt(Csquare), 2)
    # function math.sqrt is called from import math  
    return C
main()
