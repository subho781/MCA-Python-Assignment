#this program calculates the simple interest
p = float(input("Enter the principle amount: ")) 
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time period: "))
print("\nThe given values are:\n" 
        "Principle: {p} \n"
        "Rate of interest: {r} % \n"
        "Time period: {t} \n")

i = (p*r*t)/100 
print("The amount of interest is",i)
