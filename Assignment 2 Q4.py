# taking user input
ch = input("Enter a character: ")

if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
elif(ch=='B' or ch=='b' or ch=='C' or ch=='c' or ch=='D' or ch=='d' or ch=='F' or ch=='f' or ch=='G' or ch=='g' 
or ch=='H' or ch=='h' or ch=='J' or ch=='j' or ch=='K' or ch=='k' or ch=='L' or ch=='l' or ch=='M' or ch=='m' or ch=='P' or ch=='p'
or ch=='N' or ch=='n' or ch=='Q' or ch=='q' or ch=='R' or ch=='r' or ch=='S' or ch=='s' or ch=='T' or ch=='t' or ch=='V' or ch=='v'
or ch=='W' or ch=='w' or ch=='X' or ch=='x' or ch=='Y' or ch=='y' or ch=='Z' or ch=='z'):
    print(ch, "is a Consonant")
else:
    print('invalid character')