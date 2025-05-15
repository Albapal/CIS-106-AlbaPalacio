
def highlow(lastn, score):
    L=len(lastn)
    hiindex=0
    lowindex=0
    hiscore=float(-1)
    lowscore=float(99999999.99)
    for y in range(0,L,1):
        if float(score[y]) > hiscore:
            hiindex = y
            hiscore = score[y]
        if float(score[y]) < lowscore:
            lowindex = y
            lowscore = score[y]

    #Print highest score
    print("highest score", lastn[hiindex], score[hiindex])
    #Print lowest score
    print("Lowest score", lastn[lowindex], score[lowindex])


#open file and connect
f=open(r"c:\Users\Alba Palacio\Desktop\CYBERSECURITY\Programming fundamentals\Week 11\examscore.txt")

#define arrays
lastn =[]
score= []

lastname = f.readline()
for line in f:
    # Strip and split by whitespace
    parts = line.strip().split()
    
    # Ensure the line has exactly 2 parts: name and score
    if len(parts) == 2:
        name, score_str = parts
        score_value = float(score_str)
        lastn.append(name)
        score.append(score_value)
f.close()


#Function call to find highest and lowest score
highlow(lastn, score)
