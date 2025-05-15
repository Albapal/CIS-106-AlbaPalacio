def compmilespergallon(milestraveled,gallonsused):
    milespergallon=milestraveled/gallonsused
    return milespergallon
numofentries=0

r=input("Do you want to continue (y/n)?")
while r=="y":
    city=input("Enter the destination city: ")
    milestraveled = float(input("Enter the Miles Traveled: "))
    gallons = float(input("Enter the Gallons Used: "))
    milespergallon=compmilespergallon(milestraveled,gallons)
    numofentries=numofentries+1
    print("Destination City: ", city)
    print("Miles Traveled: ", milestraveled)
    print("Miles per Gallon: ", milespergallon)
    r=input("Do you want to continue (y/n)?")
print("The Number of Players Entered is: ", numofentries)

    