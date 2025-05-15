def compSalesReport(sales):
    
    commissionPercent = 0.0
    if(sales>=100000):
        commissionPercent = 0.1
    else:
        commissionPercent = 0.05
    
    commission = sales * commissionPercent
    target = sales * 1.05
    return commission, target


lastName=input("Enter Sales Person Last Name: ")
sales = float(input("Enter Sales: "))

commission, target =compSalesReport(sales)

print(f"Sales Person : {lastName} - Sales Commission : {commission:.2f} - Sales Target : {target:.2f}")
    