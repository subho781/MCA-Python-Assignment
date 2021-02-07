#WAP to input marks of 5 subject and find average and assign grade
sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: O")
elif(avg>=80 and avg<=89):
    print("Grade: E")
elif(avg>=70 and avg<=79):
    print("Grade: A")
elif(avg<70):
    print("Grade: B")