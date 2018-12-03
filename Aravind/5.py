while 1==1:
    try:
        num = input("Enter a Number : ")
        min = input("Enter Min Value : ")
        max = input("Enter Max Value : ")
        for i in range(min, max + 1):
            print num, "*", i, "=", num * (i)
    except:
        print "Enter Numbers only"
    else:
        break;