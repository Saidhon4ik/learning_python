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



#####countdown timer
import time
my_time = int(input("Enter a time in seconds: "))

for i in range(my_time, 0,-1):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("hello")