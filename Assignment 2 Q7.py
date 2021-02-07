#WAP to input 3 numbers and find the second smallest.
num1=int(input("Enter the first number: ")) 
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: ")) 
if(num1<=num2 and num1<=num3):   
  s2=num1
elif(num2<=num1 and num2<=num3):
  s2=num2
else:
    s2=num3
    print('second smallest number is :',s2)