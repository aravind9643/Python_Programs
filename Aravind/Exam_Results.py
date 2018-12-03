def read_marks_fun():
    marks = input("Enter Marks")
    return marks
def greater_than_hundred_fun():
    print "But Greater than 100 is not Allowed"
def less_than_zero_fun():
    print "Negative Marks not Allowed"

def fail_result_fun():
    if (marks < 0):
        less_than_zero_fun()
    elif (marks == 0):
        print "Your Marks : 0 and You are Failed"
    elif (marks > 0 and marks < 35):
        print "You are Failed"
def pass_result_fun():
    if (marks >= 35 and marks < 50):
        print "Third Division"
    elif (marks >= 50 and marks < 70):
        print "Second Division"
    elif (marks >= 70 and marks < 90):
        print "Passed : First Division"
    elif (marks >= 90 and marks < 100):
        print "Distinction"
    elif (marks == 100):
        print "You are Great 100%"
    elif (marks > 100):
        greater_than_hundred_fun()
def absent_fun():
    print "Sorry you are absent to the Exam please reappear"

def invalid_option_fun():
    print "Invalid Option"

def results_fun(marks):
    if(marks<0):
        fail_result_fun()
    elif(marks>0 and marks<35):
        print "Failed"
        fail_result_fun()
    elif(marks>=35 and marks<=100):
        print "Passed"
        pass_result_fun()
    elif(marks > 100):
        pass_result_fun()



attended = raw_input("Did you Attend to the Exam (Y/N),(y/n),(1,0),(true,false)")
if(attended.upper() == 'Y'):
    try:
        marks = read_marks_fun()
        results_fun(marks)
    except NameError:
        print "Invalid Marks"
elif(attended.upper() == 'N'):
    absent_fun()
elif(attended == "1"):
    try:
        marks = read_marks_fun()
        results_fun(marks)
    except NameError:
        print "Invalid Marks"
elif(attended == "0"):
    absent_fun()
elif(attended == "true"):
    try:
        marks = read_marks_fun()
        results_fun(marks)
    except NameError:
        print "Invalid Marks Only numbers are Allowed"
elif (attended == "false"):
    absent_fun()
else:
    invalid_option_fun()

