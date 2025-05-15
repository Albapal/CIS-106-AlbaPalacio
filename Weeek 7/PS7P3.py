#Open the File using raw string to avoid backslash issues. This tells Python to treat backslashes as literal characters
f=open(r"c:\Users\Alba Palacio\Desktop\CYBERSECURITY\Programming fundamentals\Week 7\data.txt", "r")

#Read the first line (lastname)
lastname = str(f.readline().rstrip('\n'))  # rstrip removes the return line feed character \n from the string input so we do not process it
totalbonus=0

#Loop through the file
while lastname !="":
    salary=float(f.readline())
    if not salary:
        break #If there is no Salary the program break
    
    #Determine the Bonus Rate
    if salary >= 100000:
        bonusrate=0.20
    else:
        if salary == 50000:
            bonusrate=0.15
        else:
            bonusrate=0.10
    #Calculate Bonus
    bonus=salary*bonusrate
    totalbonus=totalbonus+bonus

    print("The Lastname is: ", lastname)
    print("The Bonus Rate is: ", bonusrate)
    print(f"The Bonus is: ${bonus:.2f}")
    print ()
    #Read the next lastname
    lastname=str(f.readline().strip('\n'))
f.close()
#when the cycle ends print the last variable
print("The sum of all bonuses paid out is: ", totalbonus)