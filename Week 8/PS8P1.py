def compextprice(qty,unitprice):
    extprice=float(qty)*float(unitprice)
    if extprice > 10000.00:
        discam = extprice*0.10
    else:
        discamt=0.0
    return extprice
totalextprice=0.0
r=input("Do you want to compute extended price (y/n)?")

while r=="y":
    qty=float(input("Enter the quantity:"))
    unitprice = float(input("Enter Unit Price: "))
    extprice=compextprice(qty,unitprice)
    totalextprice=totalextprice + extprice
    print("Extended Price is: ", extprice)
    r=input("Do you want to compute extended price (y/n)?")
print("Total Extended Price is: $", totalextprice)

    