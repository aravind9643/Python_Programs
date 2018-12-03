str1 = raw_input("Enter First String")
str2 = raw_input("Enter Second String")
print "Common Letters in ", str1, " & ", str2, " are"
for i in str1:
    for j in str2:
        if i == j:
            print i,
