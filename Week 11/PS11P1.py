def displaynames(lastn):
       for i in lastn:
        print(i)

def displaynamesreverse(lastn):
    for i in reversed(lastn):
        print(i)   
        
#open file and connect
f=open(r"c:\Users\Alba Palacio\Desktop\CYBERSECURITY\Programming fundamentals\Week 11\lastnamereverse.txt")

#define arrays
lastn =[]

lastname = f.readline()

while lastname:
    lastn.append(lastname.rstrip())
    lastname=f.readline()
f.close()

#call the function to display the array elements
print("display names in the order of the file")
displaynames(lastn)
print("")
print("display names in Reverse")
displaynamesreverse(lastn)
#except FileNotFoundError:
#    print(f"Error: The file '{fFileNotFoundError}' was not found.")
#    exit()