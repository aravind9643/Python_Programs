class A:
    def dis1(self):
        print "A Class"

class B:
    def dis2(self):
        print "B Class"

class C:
    def dis3(cls):
        print "C Class"

class D(A,B,C):
    def dis4(cls):
        print "D Class"

print D().dis1()
