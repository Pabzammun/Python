# Functions 
def greet(name):
    print ("Hello," + name)
    
greet("Pablo")

def personal(name, job):
    print ("Hello," + name)
    print ("You are a, " + job)
    
personal("Pablo", "Devops")


def area_triangle (base, height):
    return base*height/2

area_a = area_triangle(5 , 6)
area_b = area_triangle(6, 7)

sum_areas = area_a + area_b
print("The total areais : " , sum_areas)

def time(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = (seconds - hours * 3600) - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = time(5000)
print ( hours, minutes, seconds)


#Comparing
print(1 == 1)
print (1 != 2)
print(1 < int("2"))

print(1 > 3 and 6 > 8) #Bouth of them needs to be right 
print (not 2 > 1) #Inverts the value of the expression that its right after it 
print (5 < 6 or "Hello" == "Bye")

# ==    (equality) 
# !=     (not equal to) 
# >       (greater than)
# <      (less than)
# >=    (greater than or equal to)
# <=    (less than or equal to)

# ==  Equality operator
# a == b a is equal to b
# != Not equal to operator
# a != b a is not equal to b
# > Greater than operator 
# a > b a is larger than b
# >= Greater than or equal to operator 
# a >= b  a is larger than or equal to b
# < Less than operator 
# a < b a is smaller than b
# <= Less than or equal to operator 
#a <= b a is smaller than or equal to b


#if Statements
name = "Pabloski"
if len(name) < 7 :
    print ("The name is to short, must have at least 7 characters")
elif len(name)>10:
    print ("Your user name its to long please use a shroter one")
else:
    print("Your user name have been created correctly")



number = 4
if number * 4 < 15:
    print  (number/4)
elif number < 5:
    print(number + 3)
else:
    print(number * 2 % 5)
    
n = 4 
if n*6 > n**2 or n%2 == 0:
    print("Check")
    
x = 0 
while x < 5:
    print ("Not yet, x=", x )
    x=x+1
 
 
#Loops 
    
def number(n):
    x=1
    while x <= n:
        print("The number is higher, there are", n-x , "positions of diference")
        x+=1
    print("Done")
number(6)
    
for x in range(5):
    print(x)

friends = ['Pepe', 'Pablo', 'Javi', 'Eli', 'Antonio']
for friend in friends:
    print("Hello,", friend)
    
def to_celsius(numbers):
    return (numbers-32)*5/9

for numbers in range(0, 101, 10):
    print(numbers, to_celsius(numbers))
    
    
teams = ['Pandas', 'Dragons', 'Bulldogs', 'Unicorns', 'Wolves']

for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print (home_team, " VS ", away_team)
            
            
name = 'Pablo'

print(name[len(name)-1])

file = 'File.txt'

print(file[4:8])