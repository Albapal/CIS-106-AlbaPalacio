def compnextmonthforecast(month, sales):
    forecastpercent = 0.0

    if month.upper()=="JAN" or month.upper()=="FEB" or month.upper()=="MAR":
        forecastpercent=0.10
    else:
        if month.upper()=="APR" or month.upper()=="MAY" or month.upper()=="JUN":
            forecastpercent=0.15
        else:
            if month.upper()=="JUL" or month.upper()=="AUG" or month.upper()=="SEP":
                forecastpercent=0.20
            else:
                if month.upper()=="OCT" or month.upper()=="NOV" or month.upper()=="DEC":
                    forecastpercent=0.25
                else:
                    return -1
        
    nextmonthsales=sales*(1+forecastpercent)
    return nextmonthsales


r=input("Do you want to continue (y/n)?")
while r=="y":
    lastname=input("Enter Lastname: ")
    month = input("Enter Month: ")
    sales = float(input("Enter Sales: "))
    nextmonthsales=compnextmonthforecast(month, sales)
    if nextmonthsales >0:        
        print(f"Next Month Sales: {nextmonthsales:.2f}")
    else:
        print("Month Invalid")
    r=input("Do you want to continue (y/n)?")
