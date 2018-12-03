num = input("Enter a number")
num2 = num
rev = 0
while(num != 0):
    r = num % 10
    rev = r + rev * 10
    num = num / 10
print "Reverse of Given Number : ",rev
if(num2 == rev):
    print "Entered Number is Palindrome"
else:
    print "Entered Number is Not Palindrome"