def compDiscounts(quantity,price,discountRate):
    
    discountAmount = quantity * discountRate
    discountPrice = price * discountRate
    return discountAmount, discountPrice


quantity=float(input("Enter Quantity: "))
price = float(input("Enter Price: "))
discountRate = float(input("Enter Discount Rate: "))
discountAmount, discountPrice =compDiscounts(quantity,price,discountRate)

print(f"Quantity : {quantity:.2f} - Discount Amount : {discountAmount:.2f}")
print(f"Price : {price:.2f} - Discount Price : {discountPrice:.2f}")
    