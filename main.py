# #####variables  

# #String
# first_name = "Bro"

# #int
# age = 20

# #float 
# pi = 3.14

# #boolean
# is_student = True

# if is_student:
#     print("You are a student")

# else:
#     print("You are not a student")




# #####user input
# name = input("what's your name?: ")
# age = (input("how old are u buddy?: "))
# print(f"sup {name}")
# print(f"You are {age} years old")


# #####if-statement
# response = input("Would you like some food? (Yes or No): ")
# if response == "yes":
#     print("Have some food")
# else:
#     print("No food for u then 😭")



# #####conditional expressions
# num = 5
# a = 6
# b = 7

# max_num = a if a > b else b
# min_num = b if a > b else a
# print("positive" if num > 0 else "Negative")
# result = "even" if num%2 == 0 else "odd"
# print(result)
# print("even" if num%2==0 else "odd")

# print(f"max num is {max_num}")
# print(f"min num is {min_num}")



# #####String methods 
# name = input("Enter your full name: ")
# phone_number = input("Enter your phone number: ") 

# print(len(name))
# print(name.find(" "))
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())


# print(phone_number.count("-"))
# print(phone_number.replace("-", " "))



# #small exercise
# username = input("Enter your username: ")

# if len(username>12):
#     print("your username must have less than 12 characters")
# elif not username.find(" ") == - 1:
#     print("You cannot have that username, try again please")
# elif not username.isalpha():
#     print("Your username cannot contain numbers, try again please")
# else:
#     print(f"welcome {username}")





# #####indexing
# card_number = "1234-5678-9012-3456"
# print(card_number[0])
# print(card_number[0:4])
# print(card_number[5:9])
# print(card_number[5:])
# print(card_number[-1])
# print(card_number[::2])

# last_digits = card_number[-4:]
# print(last_digits)





# #####format specifier
# price1 = 3.1415926535
# price2 = 1.134100912
# price3 = -4.123124


# print(f"{price1:.2f}")
# print(f"{price2:.2f}")
# print(f"{price3:,.2f}")



#####while loops
# name = input("Enter your name: ")
# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")
# print(f"Hello {name}")



# age = int(input("Enter your age"))
# while age < 0:
#     print("You are cannot be negative")
#     age = int(input("Enter your age: "))

# print(f"you are {age} years old")


# food = input("Enter a food you like(q for quit): ")
# while not food == "q":
#     print(f"you like {food}")
#     food = input("Enter a food you like(q for quit): ")
# print("bye")




# #####for loopss
# for i in range(1,11,2):
#     print(i)



# #####countdown timer
# import time
# my_time = int(input("Enter a time in seconds: "))

# for i in range(my_time, 0,-1):
#     seconds = i % 60
#     minutes = int(i / 60) % 60
#     hours = int(i/3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("hello")




#####nested loops

# rows = int(input("Enter the # of rows: " ))
# columns = int(input("Enter the # of columns: " ))
# symbol = input("Enter a symbol to use: ")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end=" ")
#     print()

# rows = 5

# for i in range(1, rows + 1):
#     for j in range(rows - i):
#         print(" ", end=" ")
#     for k in range(i):
#         print("*", end=" ")
#     print()







#####collections Lists[] -- changeable, ordered
# tuples() - ordered and unchangeable, duplicates ok
#  sets{} -  unordered and immutable, but fine to add or remove, no duplicates



# fruits = ["apple","banana","orange","coconut"]

# fruits[0] = "pineapple"
# fruits.append("apple")
# fruits.remove("orange")
# fruits.insert(0, "potatoXD")
# fruits.sort()
# fruits.reverse()
# # fruits.clear()
# print(fruits.index("apple"))

# for fruit in fruits:
#     print(fruit, end = " ")



# fruits = {"apple","banana","orange","coconut"}

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop() #removes the first one , but it is random
# fruits.clear()




# print(fruits)




# fruits = ("apple","orange","banana","coconut")
# print("pineapple" in fruits)
# print(fruits.index("apple"))
# print(fruits.count("coconut"))











###### 2D collections, 
# fruits = ["apple","orange","banana","coconut"]
# vegetables = ["celery","carrots","potatoes"]
# meats = ["chicken","fish","turkey"]

# groceries = [fruits, vegetables, meats]

# for collection in groceries:    
#     for food in collection:
#         print(food, end = " ")
#     print()



# num_pad = ((1,2,3),
#            (4,5,6),
#            (7,8,9),
#            ("*",0,"#"))


# for row in num_pad:
#     for num in row:
#         print(num,end = " ")
#     print()





# #####dictonaries = collection of {key:value} ordered and changeable, no duplicates are allowed
# capitals = {"USA" : "Washington DC",
#             "India": "New Delhy",
#             "China" : "Beijing",
#             "Russia": "Moscow"}

# print(dir(capitals))


# print(capitals.get("USA"))


# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital does not exist buddy")


# capitals.update({"Germany" : "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()


# for key in capitals.keys():
#     print(key)


# for value in capitals.values():
#     print(value)

# for key,value in capitals.items():
#     print(f"{key}: {value}")



# #####Consession stand program

# menu = {"pizza" : 3.00,
#         "nachos" : 4.50,
#         "popcorn" : 6.00,
#         "fries" : 2.50,
#         "chips": 1.00,
#         "pretzel": 3.50,
#         "soda": 3.00,
#         "lemonade": 4.25}



# cart = []
# total = 0

# print("---------MENU------------")
# for key,value in menu.items():
#     print(f"{key:10}:${value:.2f}")
# print("--------------------------")


# while True:
#     food = input("Select an item(q to quit): ").lower()
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)
    
# for food in cart:
#     total += menu.get(food)
#     print(food, end = " ")

# print()
# print(f"total is {total}")




# import random
# low = 1 
# high = 100

# options = ("rock","paper","scissors")
# cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

# random.shuffle(cards)
# print(cards)

# option = random.choice(options)

# number = random.randint(low,high)
# num = random.random()

# print(number)
# print(option) 






# #####functions, basics

# def happy_birthday(name,age):
#     print(f"Happy birthday {name}")
#     print(f"you are now, {age} years old")


# happy_birthday("Bro",40)



# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"your bill of ${amount:.2f} is due: {due_date} ")

# display_invoice("Bro Code", 42.50, "01/01/2001")



# #return
# def add(x,y):
#     z = x+y
#     return z

# def substract(x,y):
#     z = x-y
#     return z

# def divise(x,y):
#     z = x/y
#     return z

# def multilpy(x,y):
#     z = x*y
#     return z


# print(add(1,2))
# print(substract(1,2))
# print(multilpy(1,2))
# print(divise(1,2))



# def create_name(first,last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last   

# full_name = create_name("misha","potatovich")

# print(full_name)




# ##### default argument
# def net_price(list_price,discount=0, tax=0.05):
#     return list_price * (1-discount) * (1+tax)

# print(net_price(500))
# print(net_price(500,0.1))
# print(net_price(500,0.1,0))


# import time

# def count(end, start=0):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)


# count(10)


# #####keyword arguments

# def hello(greeting,title,first,last):
#     print(f"{greeting} {title} {first} {last}")

# hello(greeting= "Hello",title = "Mr.", first = "Spongebob", last ="Squarepants") 


# for x in range(1,11):
#     print(x, end = " ")



# print("1","2","3","4","5", sep= "@")



# def get_phone(country_code,area,first,last):
#     return f"{country_code}-{area}-{first}-{last}"

# phone = get_phone(country_code=1,area=123,first=456, last=7890)

# print(phone)




#lowkey, args is tuple and kwargs is a dictionary. Ig that's the most important shyt to remember. we gotta sorta open them up
# if we want to use them gng




#####*args 
# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1,2,3,4,5))


# def display_name(*args):
#     for arg in args:
#         print(arg, end= " ")

# display_name("Dr.","Spongebob","Squarepants")




# #####**kwargs
# def print_address(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)

# print_address(street="123 Potato St.",
#               apt = "100",
#               city ="Detroit",
#               state ="MI",
#               zip ="54321")


# def shipping_label(*args,**kwargs):
#     for arg in args:
#         print(arg, end = " ")
#     print()

#     if "apt" in kwargs:
#          print(f"{kwargs.get('street')} {kwargs.get('apt')}")
#     else:
#          print(f"{kwargs.get('street')}")

   
#     print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")


# shipping_label("Dr.","Spongebob","Squarepants","III",
#                street = "123 Banana St.",
#                apt = "#100",
#                city = "Detroit",
#                state = "Texas",
#                zip = "54321")


#I actually like args and kwargs, tho, i guess, they are a bit tricky




# #####iterables 
##TUPLES AND LISTS
# numbers = (1,2,3,4,5)

# # for number in reversed(numbers):
# #     print(number)

# for number in numbers:
#     print(number)



# fruits = {"apple","orange","coconut","banana"}

# for fruit in fruits:
#     print(fruit)


###WITH STRING
# name = "Bro Code"

# for character in name:
#     print(character, end = ' ')



# my_dictionary = {"A" : 1,
#                  "B" : 2,
#                  "C" : 3}


# for key,value in my_dictionary.items():
#     print(f"{key}:{value}")



###Membership operators = used to test if there's a value in a sequence


# #in a string
# word = "APPLE"

# letter = input("Guess a letter in a secret word: ")
# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found in our secret word")



# #in a set
# students = {"Spongebob","Patrick","Sandy"}
# student = input("Enter the name of the student: ")

# if student in students:
#     print(f"{student} is a student")

# else:
#     print(f"{student} was not found")


# #in dictionaries

# grades = {"Sandy":"A",
#           "Squidward":"B",
#           "Spongebob" : "C",
#           "Patrick": "D"}

# student = input("Enter the name of the student: ")
# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")



# #idk
# email = "BroCode@gmail.com"

# if "@" in email and "." in email:
#     print("Valid email")
# else:
#     print("Invalid email")




###list comprehension

# #wrong
# doubles = []
# for x in range(1,11):
#     doubles.append(x*2)
    
# print(doubles)


#correct one
# doubles = [x*2 for x in range(1,11)]
# print(doubles)


# triples = [y*3 for y in range(1,11)]
# print(triples)


# squares = [x**2 for x in range(1,11)]
# print(squares)


# fruits = ["apple","orange","banana","coconut"]
# fruit_chars = [fruit[0] for fruit in fruits]

# print(fruit_chars)  


# numbers = [1,-2,3,-4,5,-6]

# positive_nums = [num for num in numbers if num >= 0]
# negative_nums = [num for num in numbers if num < 0]
# even_nums = [num for num in numbers if num % 2 == 0]
# odd_nums = [num for num in numbers if num % 2 == 1]

# print(positive_nums)
# print(negative_nums)
# print(even_nums)





# grades = [85,42,79,90,56,61,30]
# passing_grades = [grade for grade in grades if grade >= 60]

# print(passing_grades)






# #####match case (switch)
# def day_of_week(day):
#     match day:
#         case 1:
#             return "it is Monday"
#         case 2:
#             return "it is Tuesday"
#         case 3:
#             return "it is Wednesday"
#         case 4:
#             return "it is Thursday"
#         case 5:
#             return "it is Friday"
#         case 6:
#             return "it is Saturday"
#         case 7:
#             return "it is Sunday"
#         case _:
#             return "not a valid day"
        

# print(day_of_week(1))



# ####module
# import math as m ### alias 'm'
# #we also can make some variables in other file and import them with 'from name_of_the_file.py import #then function ' or just 'import name_of_the_file.py
# print(m.pi)



# #####scope resolution
# #variable scope is where variable is visible and accessible
# #scope resolution (LEGB - briefly for the next thing ---> ) Local -> Enclosed -> Global -> Built-in
# def func1():
#     x = 1
#     print(x)

# def func2():
#     x = 2 
#     print(x)

# x = 3

# func1()
# func2()


# from math import e

# def func3():
#     print(e)

# e = 3 
# func3()




#### if name == "__main__": <----- what is it?
#it usually means   that that code can be imported 
#functions and classes in this module can be reused without the main block of code executing


# ####banking program

# def show_balance(balance):
#     print(f"your balance is ${balance:.2f}")

# def deposit(balance):
#     amount = float(input("Enter an amount to be deposited: "))
#     if amount < 0:
#         print("That is not a valid amount")
#         return 0
#     else:
#         return amount

# def withdraw(balance):
#     amount = float(input("Enter an amount to be withdrawn: "))

#     if amount > balance:
#         print("Insufficient funds")
#         return 0
#     elif amount < 0:
#         print("Amount must be greater than 0")
#         return 0
#     else:
#         return amount


# def main():
#     balance = 0
#     is_running = True


#     while is_running:
#         print("Python Banking program")
#         print("1. Show balance")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Exit")

#         choice = input("Enter your choice(1-4): ")
#         if choice == "1":
#             show_balance(balance)
#         elif choice == "2":
#             balance += deposit(balance)
#         elif choice == "3":
#             balance -= withdraw(balance)
#         elif choice == "4":
#             is_running = False
#         else:
#             print("That is not a valid choice, try another one")
    
#     print("Have a nice day")


# if __name__ == "__main__":
#     main()




# ######OOP in python
# from Car import Car
# car1 = Car("Mustang",2024,"Red",False)
# car2 = Car("Nexia",2016,"Blue",True)
# car3 = Car("Matiz",2012,"White",True)


# print(car1.color)
# print()



# car1.drive()
# car2.drive()
# car3.drive()


# print()
# car1.stop()
# car2.stop()
# car3.stop()


# print()
# car1.describe()
# car2.describe()
# car3.describe()




# #class variables
# class Student:

#     class_year = 2024
#     num_students = 0

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         Student.num_students += 1

# student1 = Student("Spongebob", 30)
# student2 = Student("Patrick", 35)
# student3 = Student("Squidward" , 38)
# student4 = Student("Mr.Crabs", 45)


# print(f"My graduating class of {Student.class_year} has {Student.num_students} students")



# ####Inheritance
# class Animal:
#     def __init__(self,name):
#         self.name = name
#         self.is_alive = True

#     def eat(self):
#                 print(f"{self.name} is eating")

#     def sleep(self):
#           print(f"{self.name} is sleeping")


# class Dog(Animal):
#       pass
# class Cat(Animal):
#       pass
# class Mouse(Animal):
#       pass


# dog = Dog("Steve")
# cat = Cat("Tom")
# mouse = Mouse("Jerry")

# print(dog.name)
# print(dog.is_alive)
# dog.eat()
# dog.sleep()


# ####multiple and multilevel inheritance
# class Animal:

#     def __init__(self,name):
#         self.name = name

#     def eat(self):
#         print(f"This {self.name} is eating")
#     def sleep(self):
#         print(f"This {self.name} is sleeping")
# class Prey(Animal):
#     def flee(self):
#         print(f"This {self.name} is fleeing")
# class Predator(Animal):
#     def hunt(self):
#         print(f"This {self.name} is hunting")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fih(Predator,Prey):
#     pass


# rabbit = Rabbit("Bugs")
# hawk = Hawk("Tony")
# fih = Fih("Nemo")

# rabbit.flee()
# hawk.hunt()
# print()
# fih.hunt()
# fih.flee()


# rabbit.eat()
# rabbit.sleep()

# fih.eat()
# fih.sleep()



# ######super() function

# class Shape:
#     def __init__(self,color,is_filled):
#         self.color = color
#         self.is_filled = is_filled

#     def describe(self):
#         print(f"It is {self.color} and {'filled' if self.is_filled == True else 'not filled'}")

# class Circle(Shape):
#     def __init__(self,color,is_filled,radius):
#         super().__init__(color, is_filled)
#         self.radius = radius

#     def describe(self):
#         print(f"It is a circle with an area of {3.14 * self.radius * self.radius} cm^2")
#         super().describe()

# class Square(Shape):
#     def __init__(self,color,is_filled,width,):
#         super().__init__(color, is_filled)
#         self.width = width

#     def describe(self):
#         print(f"It is a square with an area of {self.width * self.width/2} cm^2")
#         super().describe()
            
# class Trinagle(Shape):
#     def __init__(self,color,is_filled,width, height):
#         super().__init__(color, is_filled)
#         self.width = width
#         self.height = height


#     def describe(self):
#         print(f"It is a triangle with an area of {self.width * self.width/2} cm^2")
#         super().describe()


# circle = Circle(color = "red", is_filled= True, radius= 5)
# square = Square(color = "blue", is_filled= False, width= 5)
# triangle = Trinagle(color = "white", is_filled = False, width = 3, height = 4)


# print(circle.color)
# print(circle.is_filled)
# print(circle.radius)


# print()
# print(square.color)
# print(square.is_filled)
# print(square.width)
# print()



# square.describe()
# triangle.describe()
# circle.describe()






# ######Polymorphism
# from abc import ABC, abstractmethod
    
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass


# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# class Square(Shape):
#     def __init__(self,side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

# class Triangle(Shape):  
#     def __init__(self,base, height):
#         self.base = base
#         self.height = height

#     1
#     def area(self):
#         return self.base * self.height * 0.5

# class Pizza(Circle):
#     def __init__(self,topping,radius):
#         super().__init__(radius)
#         self.topping = topping


# shapes = [Circle(4), Square(5), Triangle(3,4),Pizza("peperoni",5)]

# for shape in shapes:
#     print(f"Area is {shape.area()} cm^2")



# #####duck typing, for now i have no idea wth even is this thing gng
# class Animal:
#     alive = True

# class Dog(Animal):
#     def speak(self):
#         print("Woof!")

# class Cat(Animal):
#     def speak(self):
#         print("Meow!")

# class Car:
#     def speak(self):
#         print("HONK!")

# animals = [Dog(),Cat(),Car()]

# for animal in animals:
#     animal.speak()
#     print(animal.alive)

# #so, I would sum up all of that with the fact duck typing is sort of polymorphism
# #which requires a minimum necessary attributes or methods
# # it is like, well, it can woof, it looks , sort of , like a dog, then... it is a dog?...
# #my interpretation might be wrong tho... Tho it is my personal opinion on that



# #####static method


# class Employee:

#     def __init__(self,name,position):
#         self.name = name
#         self.position = position

#     def get_info(self):
#         return f"{self.name} = {self.position}"
    
#     @staticmethod
#     def is_valid_position(position):
#         valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
#         return position in valid_positions
    
# employee1  = Employee("Eugene","Manager")
# employee2 = Employee("Squidward", "Cashier")
# employee3 = Employee("Spongebob", "Cook")


# print(Employee.is_valid_position(position="Cook"))
# print()
# print(employee1.get_info())
# print(employee2.get_info())
# print(employee3.get_info())




# ####class methods
# class Student:

#     count = 0 
#     total_gpa = 0

#     def __init__(self,name,gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1
#         Student.total_gpa += gpa


#     #Instance method
#     def get_info(self):
#         return f"{self.name} {self.gpa}"
    
#     @classmethod
#     def get_count(cls):
#         return f"Total # of students {cls.count}"
    
#     @classmethod
#     def get_average_gpa(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             return f"Average gpa: {cls.total_gpa/cls.count:.2f}"

# student1 = Student("Spongebob",3.2)
# student2 = Student("Patrick", 2.0)
# student3 = Student("Sandy", 4.0)

# print(Student.get_count())

# print(Student.get_average_gpa())




# #####magic methods
# class Book:
#     def __init__(self,title,author,num_pages):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages

#     def __str__(self):
#         return f"'{self.title}' by {self.author}"
    
#     def __eq__(self, other):
#         return self.title == other.title and self.author == other.author
    

#     def __lt__(self, other):
#         return self.num_pages < other.num_pages
    

#     def __add__(self, other):
#         return self.num_pages + other.num_pages
    

#     def __contains__(self, keyword):
#         return keyword in self.title or keyword in self.author
    

#     def __getitem__(self, key):
#         if key == 'title':
#             return self.title
#         elif key == 'author':
#             return self.author
        
#         elif key == 'num_pages':
#             return self.num_pages
#         else:
#             return f"Key {key} was not found"


# book1 = Book("The Hobbit","J.R.R Tolkien",310)
# book2 = Book("Harry Potter and the Philosopher stone","J.K Rowling",223)
# book3 = Book("The Lion,The Witch, and The Wardrobe","C.S Lewis",172)

# print(book1)
# print(book1 == book2)
# print(book1 > book2 )
# print(book1 + book2)

# print("Hobbit" in book1)

# print(book1['title'])







# #getter and setter methods 
# #@property
# class Rectangle:
#     def __init__(self,width, height):
#         self._height = height
#         self._width = width

#     @property
#     def width(self):
#         return f"{self._width:.1f} cm"


#     @property
#     def height(self):
#         return f"{self._height:.1f} cm"    
    


#     @width.setter
#     def width(self,new_width):
#         if new_width > 0:
#             self._width = new_width
#         else:
#             print("Width mmust be greater than zero")

#     @height.setter
#     def height(self,new_height):
#         if new_height > 0:
#             self._height = new_height
#         else:
#             print("Height mmust be greater than zero")




#     @width.deleter
#     def width(self):
#         del self._width
#         print("Width has been deleted")

#     @height.deleter
#     def height(self):
#         del self._height
#         print("height has been deleted")




# rectangle = Rectangle(3,4)




# rectangle.width = 4
# rectangle.height = 5


# # del rectangle.width
# # del rectangle.height

# print(rectangle.width)
# print(rectangle.height)






# #####exception in python

# #try except finally(default value)


# try:
#     number = input("enter a number: ")
#     number = int(number)

#     print(1/number)
# except ZeroDivisionError:
#     print("you cannot divide by zero, Idiot")
# except ValueError:
#     print("Enter an integer")
# except Exception:
#     print("Something went wrong")
# finally:
#     print("clean up here")
#     #it is usually used in file handling




# ######Python file detection

# import os

# file_path = "learning_python/test.txt"

# if os.path.exists(file_path):
#     print(f"The location '{file_path}' exists")

#     if os.path.isfile(file_path):
#         print("That is a file")
#     elif os.path.isdir(file_path):
#         print("That is a directory")
# else:
#     print("That location does not exist")