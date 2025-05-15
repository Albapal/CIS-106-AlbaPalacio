def comppayrate(jobcode,hoursworked):
    valhour=0
    overtime=0
    if hoursworked > 40:
        overtime = hoursworked - 40

    if jobcode=="L":
        valhour=25
    else:
        if jobcode=="A":
            valhour=30
        else:
            if jobcode=="J":
                valhour=50 
            else:
                return -1
    payrate=valhour*hoursworked
    payovertime = overtime * (valhour * 0.5)
    grosspay= payrate + payovertime
    return grosspay
totalgrosspay=0

r=input("Do you want to continue (y/n)?")
while r=="y":
    lastname=input("Enter Employee lastname: ")
    jobcode = input("Enter job Code: ")
    hoursworked = float(input("Enter Hours Worked: "))
    grosspay=comppayrate(jobcode,hoursworked)
    if grosspay >0:        
        print("Last Name: ", lastname)
        print("Gross Pay: ", grosspay)
        totalgrosspay=totalgrosspay+grosspay
        r=input("Do you want to continue (y/n)?")
    else:
        print("Job Code Invalid")
        r=input("Do you want to continue (y/n)?")

print("Total Gross Pay: ", totalgrosspay)

    