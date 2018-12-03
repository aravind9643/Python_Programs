marks = input("Enter Marks")
if(marks>=100):
    print "Marks are not valid"
elif(marks<50):
    for i in range(50):
        marks = marks+i
        if(marks == 50):
            break
    print marks
else:
    print marks