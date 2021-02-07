number = int(input(" Enter the number : "))

if((number % 5 == 0) and (number % 3 == 0)):
    print("Given Number is Divisible by 5 and 3",number)
else:
    print("Given Number is Not Divisible by 5 and 3",number)