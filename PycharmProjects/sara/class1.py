class Gyann:
    def createName(self,name):
        self.name=name
    def result(self):
        print "Hello i am % s " % self.name
f=Gyann()
f.createName('sara')
f.result()