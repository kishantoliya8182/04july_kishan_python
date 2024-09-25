# Q63. Write a Python program to returns sum of all divisors of a number.

number=int(input("Enter Number: "))

sum=0

for i in range(1,number):
    if number%i == 0:
        sum += i

print(f'Sum of All Divisors of a Number {number} is {sum}')




    