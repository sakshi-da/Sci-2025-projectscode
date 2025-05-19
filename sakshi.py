#1. Check if a number is positive or negative.

num= int(input("enter number"))
if num==0:
    print('The number is zero')
elif num>0:
    print('The number is positive')
else:
    print('The number is negative')

#2. Determine if a number is even or odd.

num=int(input('enter number: '))
if num%2==0:
    print('It is an even number')
else:
    print('It is an odd number')

#3. Check if a year is a leap year.

year=int(input( "enter a year: "))

if year%4==0 and year%400==0:
    print("Yes it is leap year")

else:
    print("It is not a leap year")

#4. Compare two numbers and find the greater.

first_number= int(input('Enter the first number: '))
second_number= int(input('Enter the second number: '))

if first_number>second_number:
    print(f'The {first_number} is greater than {second_number}' )
else:
    print(f'The {second_number} is greater than {first_number}')

#5. Find the largest among three numbers.

a=int(input('Enter first number: '))
b=int(input('Enter Second number: '))
c=int(input('Enter third number: '))

if a>b and a>c:
    print(f'{a} is the largest number')
elif b>a and b>c:
    print(f'{b} is the largest number')
else:
    print(f'{c} is the largest number')

#6. Check if a character is a vowel or consonant.

vowel= ['a','e','i','o','u']

char=input('Enter an Alphabet')

for i in vowel:
    if char.lower()==i:
        print(" It is a vowel")
        break
else:
    print("It is a consonant")

#7. Determine if a number is divisible by 5 and 11.

num= int(input('Enter a number: '))

if num%5==0 and num%11==0:
    print(f'{num} is divisible by 5 and 11 both.')
elif num%5==0 and num%11!=0:
    print(f'{num} is divisible by 5 but not by 11.')
elif num%5!=0 and num%11==0:
    print(f'{num} is divisible by 11 but not by 11.')
else:
    print(f'{num} is neither divisible by 5 nor 11.')

#8. Check if a number is a multiple of both 3 and 7.


num= int(input('Enter a number: '))

if num%3==0 and num%7==0:
    print(f'{num} is a mulitple of 3 and 7 both.')
elif num%3==0 and num%7!=0:
    print(f'{num} is a multiple of 3 but no of 7.')
elif num%3!=0 and num%7==0:
    print(f'{num} is a multiple of 7 but not of 3.')
else:
    print(f'{num} is neither a multiple of 3 nor of 7.')

#9. Determine if a character is uppercase or lowercase.

char= input('Enter an alphabet')

if char==char.upper():
    print(" It is in uppercase")

else:
    print("It is in lowercase")


#10. Check if a number is a perfect square.
import math
num=int(input("Enter a number: "))

root= math.sqrt(num)
#print(int(root))

if int(root)**2== num:
    print("it is a perfect square")

else:
    print("it is not a perfect sqaure")

#11. Determine if a number is a palindrome.

num= int(input("Enter a number: "))
string= str(num)
reverse= string[::-1]
#print(reverse)

if string==reverse:
    print("It is a palindrom number")

else:
    print("It is not palindrom number")

#12. Check if a number is an Armstrong number.

num= int(input(" Enter a number: "))
string=str(num)
length= len(string)
square = 0
for i in string:
    square= int(i)**length + square

#print(square)

if square==num:
    print("It is an armstrong number")

else:
    print('It is not an armstrong number')

#13. Determine if a number is prime.
num = int(input("enter a number"))
for i in range(2,num):
    if num%i==0:
        print('it is not a prime number')
        break
    elif num<=1:
        print('it is not a prime number')
else:
    print('it is a prime number')

#14. Check if a triangle is valid with given sides.

a= int(input("enter the first side of the triangle: "))
b= int(input("enter the second side of the triange: "))
c= int(input("enter the third side of the triangle: "))

if a+b>c and b+c>a and c+a>b:
    print("It is a valid triangle")
else:
    print("Invlaid side of triangle")

#15. Determine the type of triangle (equilateral, isosceles, scalene).

a= int(input("enter the first side of the triangle: "))
b= int(input("enter the second side of the triange: "))
c= int(input("enter the third side of the triangle: "))

if a!=b!=c!=a:
    print('It is a scalene triangle.')

elif a==b==c:
    print('It is an equilateral triangle.')

else:
    print('It is an isosceles triangle.')

#16. Check if a character is an alphabet or not.

char= input('enter a character: ')

alphabets="qwertyuiopasdfghjklzxcvbnm"

for i in alphabets:
    if i==char.lower():
        print('It is an alphabet.')
        break
else:
    print("it is not an alphabet.")

#17. Determine the grade based on percentage marks.

marks = float(input("Enter your percentage marks: "))

if marks <0:
    grade ="Invalid Input"
elif marks>= 90:
    grade = "A+"
elif marks>= 80:
    grade = "A"
elif marks>= 70:
    grade = "B"
elif marks>= 60:
    grade = "C"
elif marks>= 50:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")



#18. Check if a person is eligible to vote.

age= int(input("Enter the Age: "))

if age <1:
    print("Invalid age")

elif 0<age<18:
    print("Not eligible to vote.")
else:
    print("eligible to vote.")

#19. Check if a person is eligible for driving license.

age=int(input("enter your age: "))

if age >= 18:
  print("You are eligible for a driving license.")
else:
  print("You are not eligible for a driving license.")


#20. Determine the quadrant of a point in 2D plane.

x= int(input(" Enter the x-axis"))
y= int(input(" Enter the y-axis"))

if x==0 and y==0:
    print ("It lies on origin")
elif x<=0 and y<=0:
    print("It lies in 3rd qudrant.")

elif x>=0 and y>=0:
    print("It lies in 1st quadrant.")

elif x<=0 and y>=0:
    print("It lies in 2nd quadrant.")

else:
    print("It lies in 4rth quadrant")

#21. Check if a given year is a century year.

year=int(input( "enter a year: "))

if year%100==0:
    print("Yes it is century year")

else:
    print("It is not a century year")

#22. Determine if the temperature is hot, cold, or moderate.

cold_temp=20
hot_temp= 35

temp =float(input("Enter the temperature in Celsius: "))

if temp > hot_temp:
  print("The temperature is hot.")
elif temp < cold_temp:
  print("The temperature is cold.")
else:
  print("The temperature is moderate.")

#23. Find the absolute value of a number.
num= float(input("Enter a number: "))

if num >= 0:
  print(f'The absolute value is {num}')
else:
  print(f'The absolute value is {-num}')


#24. Check if a person is tall, average, or short based on height.

#25. Compare three numbers and find the smallest.
a=int(input('Enter first number: '))
b=int(input('Enter Second number: '))
c=int(input('Enter third number: '))

if a<b and a<c:
    print(f'{a} is the smallest number')
elif b<a and b<c:
    print(f'{b} is the smallest number')
else:
    print(f'{c} is the smallest number')

#26. Check if a number is within a specific range.

num= float(input("enter a number in specified range (0-30)"))

if 0<=num<=30:
    print("Yes the number exists in this specified range")

else:
    print("The number doesn't belongs to this range")

#27. Check if a day number (1-7) is a weekday or weekend.
num = int(input("Enter Number Between 1-7"))
if 0< num <6 :
    print("weekday")
elif 5< num <=7 :
    print("weekend")
else:
    print("Invalid Number!")

#28. Check if a number is a single digit, two-digit, or more.

num= int(input("Enter a number: "))
string=str(num)
length= len(string)

if length==1:
    print("It is a single digit number")

elif length==2:
    print("it is a two digit number")

else:
    print("it is more than two digit number")


#29. Determine the electricity bill based on usage.

#30. Check if a password is strong based on simple rules.
print("Create a password that is:")
print("At least 8 characters long.")
print("Contains at least one uppercase letter.")
print("Contains at least one lowercase letter.")
print("Contains at least one digit (0-9).")
print("Contains at least one special character.")

password= input("enter the password: ")

special_char= "~!@#$%^&*()_+`-=[];,./{}|:><?'"
for i in password:
    if i.isupper()==True:
        if i.islower()==True:
            if i.isdigit()==True:
                for char in special_char:
                    if i==char:
                        print("The password is strong.")
                        break
else:
     print("The password is week")



#31. Determine if a year is a leap year using nested if.

year=int(input( "enter a year: "))

if year%4==0:
    if year%400==0:
        print("Yes it is leap year")

else:
    print("It is not a leap year")


#32. Check if a number is even and divisible by 4.

num= int(input('Enter a number: '))

if num%2==0 and num%4==0:
    print(f'{num} is even and divisible by 4.')
elif num%2==0 and num%4!=0:
    print(f'{num} is even but not divisible by 4.')
else:
    print(f'{num} is neither even nor divisible by 4.')


#33. Determine if a student passed or failed.

percentage=float(input("Enter your percentage: "))

if percentage<40:
    print("Failed")

else:
    print("Passed")


#34. Check if a number ends with a specific digit.

#let us take that specified digit is 98.

num=int (input("enter a number end with 98: "))
string= str(num)
specified_digit='98'
if string.endswith(specified_digit)==True:
    print("It ends with 98")
else:
    print('it does not ends with 98.')


#35. Determine if a month number has 30 or 31 days.
a=['january','march','may','july','september','november']

month= input("Enter the name of the month: ")

for i in a:
    if i==month.lower():
        print('It has 31 days')
        break
    elif month.lower()=='february':
        print("It has 28 or 29 day")
        break

else:
    print('It has 30 days')




#36. Compare strings and check if they are equal.

first= input("enter the first string")
second= input("enter the second string")

if first.lower()==second.lower():
    print("Both the string are equal")

else:
    print("they are not equal.")


#37. Check if a string is empty or not.

input_string = input("Enter a string: ")

if not input_string:
  print("The string is empty.")
else:
  print("The string is not empty.")

#38. Determine if a character is a digit or not.

char=input("enter a character: ")

if len(char) != 1:
  print("Invalid input. Please enter a single character.")
else:
  if '0' <= char <= '9':
    print('It is a digit.')
  else:
    print("It is not a digit.")


#39. Check if the sum of two numbers is even or odd.

num1=int(input('enter frist number: '))
num2= int(input('enter second number: '))
sum= num1+num2
if sum%2==0:
    print('The sum of these two numbers is even')
else:
    print('The sum of these two numbers is odd.')


#40. Determine if the input is an integer or not.

#41. Compare the lengths of two strings.

a= input("enter the first string: ")
b= input("enter the second string: ")

if len(a)==len(b):
    print("The length of both strings are equal.")
else:
    print("The length of the strings are not equal.")


#42. Check if the first and last digit of a number are the same.

num= int(input("enter a number: "))
string= str(num)

if string[0]==string[-1]:
    print("The frist and the last digits are same")

else:
    print("The first and the last digits are not same.")


#43. Determine if a number is a Fibonacci number.
num=int(input("enter a number: "))

a=0
b=1
c=0
if num==a or num==b:
    print("It is a fibonacci number.")
else:
    while b< num:
        a=b
        b=c
        c=a+b
    if b==num:
        print("It is a fibonacci number.")
    else:
        print("It is not a fibonacci number.")


#44. Check if the given time is AM or PM.

time= input("enter the time in 24hrs: ")

if 0<=int(time)<12:
    print("The time is AM.")

elif 12<=int(time)<24:
    print("The time is PM")

else:
    print("invalid time!")


#45. Determine the season from the month number.

month= int(input ("Enter month by its number (1-12): "))

if 0<month<2 and 10<month<13:
    print("winter season")

elif 1<month<4:
    print("spring season")

elif 3<month<7:
    print("summer season")

elif month==10:
    print("autumn seasoon")

else:
    print("rainy season")


#46. Check if a given angle is acute, right, or obtuse.

angle= int(input("Enter the angle: "))

if angle==90:
    print("It is right angle.")

elif 0<angle<90:
    print("It is acute angle.")

elif 90<angle<180:
    print("It is obtuse angle")

else:
    print("Invalid or try using within 180 degrees.")
    



#47. Determine if a number is a power of 2.

num = int(input("enter the number: "))
i=0
while i<num:
    power = 2**i
    i=i+1
    if power==num:
        print("It is a power of 2")
        break
else:
    print("it is not a power of 2")


#48. Check if a character is a special symbol.

special_symbol="~~!@#$%^&*()_+`-={}|:0<>?\;][',./"

symbol= input ("enter a special symbol")
for char in special_symbol:
    if symbol==char:
        print("yes it is a special symbol")
        break

else:
    print("it is not a special symbol")


#49. Determine eligibility for a scholarship based on marks and income.

#50. Check if a sum of any two numbers is greater than the third.

a= int(input("enter the first number"))
b= int (input("enter the second number"))
c= int(input("enter the third number"))

if a+b>c:
    print( f'The sum of {a} and {b} is greater than {c}')

elif b+c>a:
    print( f'The sum of {b} and {c} is greater than {a}')

else:
    print( f'The sum of {a} and {c} is greater than {b}')
  
