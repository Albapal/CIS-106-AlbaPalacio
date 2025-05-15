def compBowlerValues(score1,score2,score3,handicapPercent):
    
    baseValue = 200

    if (score1 > baseValue or score2 > baseValue or score3 > baseValue):
        return 0,0
    #Calculate average score
    averageScore = (score1+score2+score3) / 3
    # Calculate handicap amount
    handicapAmount = (baseValue - averageScore) * handicapPercent
    averageScoreHandicap = averageScore + handicapAmount
    
    return averageScore, averageScoreHandicap


lastName=input("Enter Bowler Last Name: ")
score1 = float(input("Enter Score Game 1: "))
score2 = float(input("Enter Score Game 2: "))
score3 = float(input("Enter Score Game 3: "))
handicapPercent = float(input("Enter Handicap percentage: "))

averageScore, averageScoreHandicap =compBowlerValues(score1,score2,score3,handicapPercent)

if(averageScore == 0 and averageScoreHandicap == 0):
    print ("Invalid Score Values. Remember, the base Values is 200")
else:
    print(f"Bowler: {lastName} - Average Score : {averageScore:.2f} - Average Score with Handicap : {averageScoreHandicap:.2f}")
    