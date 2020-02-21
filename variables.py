name = ' mustafa'
my_age = ' 31'
breakfast = ' coffe'

print(name)
print(my_age)
print(breakfast)

my_age = ' 31'

print('i am' + name + my_age + ' and i like coffe' + breakfast)

print('my favorate breakfast is {} my name is {} and i am {}'.format(breakfast, name, my_age))


i = 9

print(i)
#you just add 2 to it
i+= 2
print(i)

#multiply by 9
i *= 2

print(i)
#this devide by the number you have given
i /= 2
print(i)
#this is just the remainder of the division
i %= 2

print(i)

i = 3
i **= 3

print(i)

name = 'tom'
age = '25'
color = 'blue'

print('my friend name is {} he is {} and his favorate color is {}'.format(name, age, color))


breakfast = 'egg'
lunch = 'kebab'
dinner = 'pizza'

print('i will have for breakfast {}, lunch {} and for dinner {}'.format(breakfast, lunch, dinner))

breakfast = 'coffe'
lunch = 'chicken curry'
dinner = 'rice'

print('Tomarrow i will have for breakfast {} for lunch {} and for dinner {}'.format(breakfast, lunch, dinner))


import datetime
today = datetime.date.today()
future = datetime.date(2022, 2,4)
remain = future - today
print(remain.days)


import datetime

today = datetime.date.today()
future = datetime.date(2022,1,2)
dif = future - today
print (dif.days)

#first import the libarary then today date and time then the future date then mines days from future
import datetime

today = datetime.date.today()
future = datetime.date(2021,9,2)
left = future - today
print(left.days)

today = datetime.date.today()
future = datetime.date(2021,5,1)
deff = future - today
print('its only this many days left to my birthdays {}'.format(deff.days))


print("      |         |       ")
print("  X   |    O    |       ")
print("      |         |       ")
print("------------------------")
print("      |         |       ")
print("  X   |    X    |       ")
print("      |         |       ")
print("------------------------")
print("      |         |       ")
print("  X   |         |       ")
print("      |         |       ")



age = 16
country = 'uk'
if age < 17 and country == 'uk':
    print('yes i can serve you')
else:
    print('you are not old enough')


day = 'saturday'

if day == 'saturday' or day == 'sunday':
    print('its weekend')

#challenges starts in here 

x = 'mustafa1'
if (len('{}'.format(x)) < 8 ):
    print('the password is too short')
else:
    print('{}'.format(x))

num = 7

if num % 3 or 5:
    print('This number is divisible by 3 or 5')

else:
    print('“This number is not divisible by 3 or 5')

num = 11 

if num % 3:
    print('fiss')

elif num % 5:
    print('buzz')

else:
    print('fizzbuzz')
          
num = str(input('put your number in here: '))
# def ispalindrome(num) : return num == num [::-1] 
if num == num[::-1]:
    print('{} is a palindrome'.format(num))
else:
    print('{} is not a plaindrome'.format(num))














