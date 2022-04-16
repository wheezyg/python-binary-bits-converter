x = int(input("enter number to convert to binary"))


while x:
    y = bin(x).replace("0b", "")
    z = len(y)
    print (y)
    print ("contains", z, "bits")
    x = int(input("enter number to convert to binary"))