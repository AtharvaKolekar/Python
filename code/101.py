# Write a program to reverse an integer in Python

num = int(input("Enter an integrer: "))
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed integer is: " + str(reversed_num))

### Easier Way ###
#print(str(num)[::-1])
