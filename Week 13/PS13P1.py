#Define the object
class Employee:
    #use pass to leave empty for now
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    # self.rate = 0.00
    def bonus(self,rate):
        b = float(rate) * float(self.pay)
        return b

#Main - Execution begins here
#instantiate the object
empl1 = Employee('Frank', 'Alvino', 60000.00)

#Use the Object
#object syntax is object.method
print(empl1.email)
print(empl1.first)
print(empl1.last)
print(empl1.pay)
print(empl1.bonus(0.10))
print(empl1.bonus(0.20))