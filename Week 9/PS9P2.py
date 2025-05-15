def compsquarefootage(length, width, height):
    
    squarefootage = (2*length*width)
    squarefootage += (2*length*height)
    squarefootage += (2*width*height)

    return squarefootage

totaltuitionowed=0

r=input("Do you want to continue (y/n)?")
while r=="y":
    length=float(input("Enter Length: "))
    width = float(input("Enter Width: "))
    height = float(input("Enter Height: "))
    squarefootage=compsquarefootage(length, width, height)
    gallonsRequired = squarefootage/50
    print(f"Gallons Needed : {gallonsRequired:.2f}")

    r=input("Do you want to continue (y/n)?")

    