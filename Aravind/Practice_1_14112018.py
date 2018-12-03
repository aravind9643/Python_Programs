# Functions without Return values
def sum_fun(a, b):
    c = a+b
    print "sum in sum_fun : ", c


sum_fun(10, 20)


# Functions with Return values
def sum_fun2(a, b):
    c = a+b
    return c


sum = sum_fun2(10, 20)
print "sum returned from sum_fun : ", sum


# calling functions from the same file
def display_fun():
    print "Hello"


display_fun()

# functions with parameters


def params_fun(a, b):
    print "a : ", a
    print "b : ", b


params_fun(25, 81)

# functions  without parameters


def params_fun2():
    a = 20
    b = 40
    print "a : ", a
    print "b : ", b


params_fun2()
# functions with default arguments


def params_fun3(a, b=30):
    print "sum : ", a+b


params_fun3(20)
