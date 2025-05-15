def compbataverage(numofhits,atbats):
    bataverage=numofhits/atbats
    return bataverage
numofplayers=0

r=input("Do you want to compute the average (y/n)?")
while r=="y":
    lastname=input("Enter the lastname: ")
    numofhits = float(input("Enter the Number of Hits: "))
    atbats = float(input("Enter the at bats: "))
    bataverage=compbataverage(numofhits,atbats)
    numofplayers=numofplayers+1
    print("The the lastname is: ", lastname)
    print("The Average is: ", bataverage)
    r=input("Do you want to compute the average (y/n)?")
print("The Number of Players Entered is: ", numofplayers)

    