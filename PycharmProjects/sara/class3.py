class Employee:
    def __init__(self,first,last,num,pay):
        self.first=first
        self.last=last
        self.num=num
        self.email=first+''+last+''+num+'gmail.com'
    def fn(self):
        return '{} {}'.format(self.first,self.last)
emp_1=Employee('sara','vyas','007',500000)
print(emp_1.email);
print(Employee.fn(emp_1))
print (emp_1.fn())
