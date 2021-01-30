#this program reverses the input number from user
def rev(n):
    r=0  
    while(n>0):
        a = n % 10
        r = r * 10 + a 
        n = n // 10
    return r
num = int(input("Enter the number: "))
reverse = rev(num) 
print('the reverse number of',num,'is',reverse)