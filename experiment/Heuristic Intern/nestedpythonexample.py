#A Python program to check whether a number is divisible by 2 & 3.
num= int(input("Enter a number to check the divisibility by 2 & 3.\n"))

if num % 2 == 0:
    if num % 3 == 0:
        print("The number you gave is divisible by 2 & 3.")
elif num % 2 == 0:
    print("The number you gave is divisible by 2 and not by 3.") 
elif num % 3 ==0:
    print("The number you gave is divisible by 3 not by 2.")
else:
    print("The number you gave is not divisible by 2 and 3.")
