f=open(r"c:\Users\Alba Palacio\Desktop\CYBERSECURITY\Programming fundamentals\Week 7\student.txt", "r")
#Read the first line (lastname)
lastname = (f.readline().rstrip('\n'))  # rstrip removes the return line feed character \n from the string input so we do not process it
count=0
tottuition=0
#Loop through the file
while lastname !="":
    district=(f.readline().rstrip('\n'))
    numcred=float(f.readline())
    if not numcred:
        break #If there is no Salary the program break
    
    #Determine the Cost per Credit
    if district == 'I':
        costpercredit=250
    else:
        if district == 'O':
            costpercredit=500
    #Determine the Tuition
    tuition=numcred*costpercredit
    tottuition=tottuition+tuition
    count=count+1
    #Impresion
    print("Student Las Name:", lastname)
    print("Credits Taken: ", numcred)
    print("The Tuition is: ", tuition)
    print()
    #Read the next lastname
    lastname=str(f.readline().strip('\n'))
f.close()
#when the cycle ends print the last variables
print("The sum of all Tutitions is: ", tottuition)
print("The Number of Students is: ", count)