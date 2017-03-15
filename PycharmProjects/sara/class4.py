class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
       # print self.sides

    def inputSides(self):
        self.sides = [float(input(str(i+1))) for i in range(self.n)]
            #print self.sides

    def dispSides(self):
        for i in range(self.n):
            print i+1,self.sides[i]
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        try:
            if((a+b>c) or (a+c>b) or (b+c>a)):
                s = (a + b + c) / 2
                area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
                print('%0.2f' % area)
        except ValueError:
            print "please enter correct values"
t = Triangle()

t.inputSides()

t.dispSides()

t.findArea()
