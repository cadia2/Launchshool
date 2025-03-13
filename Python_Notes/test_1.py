##===============================
#First Lesson
#===============================


my_list = [ 1, 'xyz', True, [2, 3, 4]]
print(my_list)

my_tuple = (1,)
print(type(my_tuple))

x = tuple(range(5))
print(x)

x = tuple(range(5))
print(x)

my_dict = {
    'title': "Monty Python's Flying Circus",
    'cast': [
        'Eric Idle',
        'John Cleese',
        'Terry Gilliam',
        'Graham Chapman',
    ],
    'first_season': 1969,
    'last_season': 1974,
 }

print(my_dict['title'])
print(my_dict['cast'][2])

my_dict['first_season'] = 1000
print(my_dict['first_season']) 

s2 = {2, 3, 5, 7, 11}
print(type(s2))

s5 = frozenset([1, 2, 3])
print(s5)       

names = (
     'Asta',
     'Butterscotch',
     'Pudding',
     'Neptune',
     'Darwin',
   
)

pets = {
    'Asta':             'dog',
    'Butterscotch':     'cat',
    'Pudding':          'cat',
    'Neptune':          'fish',
    'Darwin':           'lizard',
   
}


#===============================
# Basic Operations
#===============================

print(16 // 3) #5

print(15)
print(16)
print(17)
print(18)

if 1 != 2: #not equal
    print("  1 is not equal to 2 ")

#type function

print(type(1)) #<class 'int'>
print(type(1).__name__) # int

print(type(1) is int) # True 

my_str = 'abc'
print(my_str)       # abc
print(str(my_str))  # abc (same as print(my_str))
print(repr(my_str)) # 'abc' (note the quotes)

print(len('Hello'))
print(len(['a', 'b', 'c']))

my_range = range(5,8)
print(my_range[0]) #5
print(my_range[1]) #6
print(my_range[2]) #7
#print(my_range[3]) #Object out of range

##===============================
#Exercises Basic operations
#===============================

My_full_name = 'Chris' + 'Andreopoulos'
print(My_full_name)

#4936

#Get 6
number = 4936

print(number % 10) 

number2 =str( number % 100)
print(number2[0])

number3 =str( number % 1000)
print(number3[0])

number4 =str( number % 10000)
print(number4[0])



#===============================
#Variables 
#===============================

# Naming conventions for most identifiers (excluding constant and class names)

##answer_test_2 #(all small)

# Constants are all capd e.x CONSTANT

# class names ConstantFile  

#Function example

def square(number):
    return number * number

forty_two_squared = square(42)
print(forty_two_squared)


def hello(x):
    return x + 'Hi'

greet = hello("lol")
print(greet)

def addition_3(x):
    return x + 5 + 3

add_3 = addition_3(3)
print(add_3)

#Greeter program
x = 'Victor'
print(f"Good Morning, {x}.")
print(f"Good Afternoon, {x}.")
print(f"Good Evening, {x}.")

#Age program

AGE = 22

print(f"You are {AGE} years old.")
print(f"In 10 years, you will be {AGE+10} years old.")
print(f"In 20 years, you will be {AGE+20} years old.")
print(f"In 30 years, you will be {AGE+30} years old.")
print(f"In 40 years, you will be {AGE+40} years old.")

#million euro in bank

balance = (1000 * 1.05 * 1.05 * 1.05 * 1.05 * 1.05)
print(balance)


