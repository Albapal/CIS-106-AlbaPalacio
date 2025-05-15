def displaynames(lastn, score):
    
    L=len(lastn) 

    #Display array using for loop control
    print("Display array")
    for x in range(0,L,1):
        print(x, " ", lastn[x], score[x])


#open file and connect
f=open(r"c:\Users\Alba Palacio\Desktop\CYBERSECURITY\Programming fundamentals\Week 11\examscore.txt")

#define arrays
lastn =[]
score= []

lastname=f.readline()
while lastname:
    if not lastname:
     break
    lastn.append(lastname.rstrip())
    s=(f.readline().strip())
    score.append(s)
    lastname=f.readline()
f.close()

#call the function to display the array elements
displaynames(lastn, score)
