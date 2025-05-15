def compAverageTotal(score1,score2,score3):
    
    totalPoints = score1 + score2 + score3
    average = totalPoints / 3
    return totalPoints, average


studentLastName=input("Enter Student Last Name: ")
score1 = float(input("Enter Exam Score 1: "))
score2 = float(input("Enter Exam Score 2: "))
score3 = float(input("Enter Exam Score 3: "))
totalPoints, average =compAverageTotal(score1,score2,score3)

print(f"Student : {studentLastName} - Total Points : {totalPoints:.2f} - Average : {average:.2f}")
    