def comptuitionowed(credithours,districtcode):
    valcredit=0

    if districtcode=="I":
        valcredit=250
    else:
        if districtcode=="O":
            valcredit=550
        else:
            return -1
        
    tuitionowed=valcredit*credithours
    return tuitionowed

totaltuitionowed=0

r=input("Do you want to continue (y/n)?")
while r=="y":
    lastname=input("Enter Student lastname: ")
    credithours = float(input("Enter Credit Hours: "))
    districtcode = input("Enter District Code: ")
    tuitionowed=comptuitionowed(credithours,districtcode)
    if tuitionowed >0:        
        print("Student Name: ", lastname)
        print("Tuition Owed: ", tuitionowed)
        totaltuitionowed=totaltuitionowed+tuitionowed
        r=input("Do you want to continue (y/n)?")
    else:
        print("District Code Invalid")
        r=input("Do you want to continue (y/n)?")

print("Total Tuition Owed: ", totaltuitionowed)

    