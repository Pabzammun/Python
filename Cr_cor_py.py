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