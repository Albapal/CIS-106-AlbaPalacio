def compoutthedoorprice(MSRP, make, model, ev_code):

    discountpercent = 0.0
    if(make.upper()=="HONDA" and model.upper()=="ACCORD"):
        discountpercent = 0.10
    elif(make.upper()=="TOYOTA" and model.upper()=="RAV4"):
        discountpercent = 0.15
    elif (ev_code.upper()=="Y"):
        discountpercent = 0.30
    else:
        discountpercent = 0.05
               
    discountamount = MSRP * discountpercent
    newMSRP= MSRP - discountamount
    
    return newMSRP
  

totalprice=0
msrp_total = 0
sales_price_total = 0

r=input("Do you want to start (y/n)?").lower()
while r=="y":
    make=input("Enter Make: ")
    model = input("Enter Model: ")
    ev_code = input("Enter Electric Vehicle Code (Y/N): ")
    MSRP = float(input("Enter MSRP: "))
    newMSRP=compoutthedoorprice(MSRP, make, model, ev_code)
    taxamount = newMSRP * 0.07
    totalprice = newMSRP + taxamount
    msrp_total = msrp_total + MSRP
    sales_price_total = sales_price_total+totalprice
    print(f"New Value : {totalprice:.2f}")
    

    r=input("Do you want to continue (y/n)?").lower()
print(f"Total MSRP of all cars : {msrp_total:.2f}")
print(f"Total Sales Price of all cars : {sales_price_total:.2f}")