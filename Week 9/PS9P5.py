def compAssessedValue(county,marketValue):
    
    assessedValuePercent = 0.0
    if(county.upper() == "COOK"):
        assessedValuePercent = 0.90
    elif(county.upper() == "DUPAGE"):
        assessedValuePercent = 0.80
    elif (county.upper() == "MCHENRY"):
        assessedValuePercent = 0.75
    elif (county.upper() == "KANE"):
        assessedValuePercent = 0.60
    else:
        assessedValuePercent = 0.70

    assessedValue = marketValue * assessedValuePercent
    return assessedValue

totalMarketValues=0
totalAssessedValues=0

r=input("Do you want to start (y/n)?")
while r=="y":
    county=input("Enter County: ")
    marketValue = float(input("Enter Market Value: "))
    assessedValue=compAssessedValue(county,marketValue)
    totalMarketValues += marketValue
    totalAssessedValues += assessedValue

    print(f"Assessed Value : {assessedValue:.2f}")

    r=input("Do you want to continue (y/n)?")
print(f"Total Market Values : {totalMarketValues:.2f}")
print(f"Total Assessed Values : {totalAssessedValues:.2f}")

    