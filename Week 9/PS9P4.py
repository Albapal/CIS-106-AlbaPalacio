def comptrainTicketPrice(miles):
    
    ticketPrice = 0.0
    if(miles >= 30):
        ticketPrice = 12
    elif(miles >= 20 and miles <= 29):
        ticketPrice = 10
    elif (miles >= 10 and miles <= 19):
        ticketPrice = 8
    else:
        ticketPrice = 5

    return ticketPrice

totalticketPrice=0

r=input("Do you want to start (y/n)?")
while r=="y":
    lastName=input("Enter Last Name: ")
    miles = float(input("Enter Miles: "))
    trainTicketPrice=comptrainTicketPrice(miles)

    totalticketPrice += trainTicketPrice
    print(f"Ticket Price : {trainTicketPrice:.2f}")

    r=input("Do you want to continue (y/n)?")
    print(f"The Price of all tickects are : {totalticketPrice:.2f}")

    