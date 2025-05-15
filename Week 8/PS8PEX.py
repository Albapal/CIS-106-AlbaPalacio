def comptotal(qty,price):
    total=qty*price
    if total > 10000:
        disc = total*0.10
        total=total-disc
    else:
        total=total
    return total
totextprice=0.0

r=input("Do you want to compute extended price (y/n)?")
while r=="y":
    qty=float(input("Enter the quantity:"))
    price = float(input("Enter Unit Price: "))
    total=comptotal(qty,price)
    print("The Quantity is: ", qty)
    print("The price is: ", price)
    print("The total is: ", total)
    totextprice=totextprice+total
    r=input("Do you want to compute extended price (y/n)?")
print("Total Extended Price is: $", totextprice)

    