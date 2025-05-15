def compValues(quantity,unitPrice):
    
    global total
    total = quantity * unitPrice
    global tax
    tax = total * 0.07


quantity = float(input("Enter Quantity: "))
unitPrice = float(input("Enter Unit Price: "))

compValues(quantity,unitPrice)

print(f"Total : {total:.2f} - Tax : {tax:.2f}")
    