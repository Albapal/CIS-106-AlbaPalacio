f=open(r"c:\Users\Alba Palacio\Desktop\CYBERSECURITY\Programming fundamentals\Week 7\item.txt", "r")
#Read the first line (lastname)
item = (f.readline().rstrip('\n'))  # rstrip removes the return line feed character \n from the string input so we do not process it
count=0
toextpri=0
#Loop through the file
while item !="":
    qty=float(f.readline())
    price=float(f.readline())
    if not price:
        break #If there is no Salary the program break
    
    #Determine the Extended Price
    extprice=qty*price
    count=count+1
    toextpri=toextpri+extprice
    print("The Item is: ", item)
    print("Cantidad: ", qty)
    print("The Price is: ", price)
    print("The Extended Price is: ", extprice)
    print()
    #Read the next lastname
    item=str(f.readline().strip('\n'))
f.close()
#Final Calculations
average=toextpri/count
print("The sum of all the extended prices is: ", toextpri)
print("The count of the number of orders is:", count)
print("The average order is: ", average)