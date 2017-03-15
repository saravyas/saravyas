class Gyan:
    employee = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Gyan.employee += 1
    def displaycount(self):
        print "total employee %d" %Gyan.employee
    def displayDetails(self):
        print "name",self.name,"Age",self.age
# emp1 = Gyan("Zara", 2000)
# emp2 = Gyan("Manni", 5000)
# emp1.displayDetails()
# emp2.displayDetails()
# print "Total Employee %d" % Gyan.employee
print Gyan.__doc__
print Gyan.__name__
print Gyan.__dict__
print Gyan.__module__
print Gyan.__bases__s2