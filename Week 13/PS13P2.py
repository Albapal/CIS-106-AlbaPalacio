#Define the object
class Student:
    #use pass to leave empty for now
    def __init__(self, first, last, districtcode, credits):
        self.first = first
        self.last = last
        self.districtcode = districtcode
        self.credits = credits
   
    def tuition(self):
        val=0.0
        if self.districtcode == "I":
            val=250*self.credits
        else:
            val=500*self.credits
        return val

#Main - Execution begins here
#instantiate the object
student1 = Student('Frank', 'Alvino', 'I', 4)

#Use the Object
#object syntax is object.method
print(student1.first)
print(student1.last)
print(student1.districtcode)
print(student1.credits)
print(student1.tuition())