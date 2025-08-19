number =  int(input('enter a number'))

if number % 2 ==0:
 print(f"{number} is even")
else:
    print(f"{number} is odd")


# print if positive or negative

x = int(input('Enter the number: '))

if x > 0:
    print(f"{x} is positive")
elif x < 0:
    print(f"{x} is negative")
else:
    print("Zero entered")
