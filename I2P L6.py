


#Finds and tells us the largest number
def f_larger(int1,int2):
    """This function will return the largest of the two integers"""
    if int1 >= int2:
            return int1
    else:
            return int2
x = 12
y = 7
z = 79

print(f_larger(f_larger(x,y),z))


#Making a space gap in the system box
print(""

    "")

#Finds the higher of the two numbers
def f_print_largest(int1,int2):
    """This function will print the largest of two integers"""
    if int1 > int2:
        print(int1,"is the largest")
    if int1 < int2:
        print(int2,"is the largest")
f_print_largest(12,50)
