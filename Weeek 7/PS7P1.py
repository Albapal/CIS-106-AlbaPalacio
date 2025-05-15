principal=float(input("Enter the Principle: "))
interestrate=float(input("Enter the Interest Rate: "))
totint=0
annualint=0
print("year      Beginning Balance      End Balance")
for year in range(1,6,1):
    annualint =principal*interestrate
    endbalance=principal+annualint
    totint=totint+annualint
    print(year, "         ", principal, "            ", endbalance)
    principal=endbalance
print("Total Interest:  ", totint)