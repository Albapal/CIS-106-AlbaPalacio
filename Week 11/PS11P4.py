
def showArrays(lastn, average):

    for i in lastn, average:
       print(i)

def findBaller(lastname,lastn, average):

    L=len(lastn)
    for y in range(0,L,1):
        if (lastn[y] == lastname):
            print (f"{lastn[y]} has an Average of {average[y]:.3f}")


#open file and connect
f=open(r"c:\Users\Alba Palacio\Desktop\CYBERSECURITY\Programming fundamentals\Week 11\batAverage.txt")

#define arrays
lastn =[]
average= []

#Fill the arrays
lastname = f.readline()
for line in f:
    # Strip and split by whitespace
    parts = line.strip().split()
    
    # Ensure the line has exactly 2 parts: name and score
    if len(parts) == 2:
        name, average_str = parts
        average_value = float(average_str)
        lastn.append(name)
        average.append(average_value)
f.close()

#Function to print tha arrays
showArrays(lastn, average)

follow = "y"

while follow=="y":
    lastname =input("Last name : ")
    findBaller(lastname,lastn, average)
    follow=input("Do you want to continue (y/n)?")
