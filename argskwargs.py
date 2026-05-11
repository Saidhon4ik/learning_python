#====================#
#example 1 with args
def add(*args):
          total = 0
          for arg in args:
                  total+= arg
          return total

print(add(1,2,31,23,12312,3,1))
#====================#








#=======================================#
#2
#*args allow you to pass multiple non-key arguments
#**kwargs allows you to pass multiple key-word arguments
#1. positional 2. default 3. keyword 4.ARBITRARY 
def display_name(*args):
        for arg in args:
                print(arg, end = " ")

display_name("Dr.","Spongebob","Harold","Squarepants")
#=======================================#




#==========================#
#3
def print_address(**kwargs):
        for key,value in kwargs.items():
                print(f"{key}: {value}")


print_address(       street ="123 Potato st",
                              city ="Detroied",
                              state = "MI",
                              zip="54312")
#==========================#




#==========================#
#4 
def shipping_label(*args,**kwargs):
        for arg in args:
                print(arg,end = " ")
        print()

        if "apt" in kwargs:
                    print(f"{kwargs.get('street')} {kwargs.get('apt')}")
        else:
                    print(f"{kwargs.get('city')}")
             
        print(f"{kwargs.get('city')}, {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr","Spongebob","Squarepants","III",
               street = "123 Potato St.",
               apt = "100",
               city = "Detroir",
               state = "MI",
               zip = "54321")