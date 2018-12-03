marks = input("Enter Marks")

if marks>40 and marks<60:
    hike = 0
elif marks>60 and marks<80:
    hike = marks*10/100
elif marks>80 and marks<90:
    hike = marks*20/100
else:
    hike = marks*30/100

print hike