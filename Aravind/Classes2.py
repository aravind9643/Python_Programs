class A:
    __a = 10
    x = 50
    def display(self):
        print self.__a
        print "this is display function"

# x = A()
# x.x = 20
# print x.x

y = A()
print y.x
print y.display()