# #===============================WRITING FILES =============== WRITING FILES=====================================

# #####for csv
# import csv

# employees = [["Name","Age","Job"],
#              ["Spongebob",30,"cook"],
#              ["Patrick",37,"Unemployed"],
#              ["Sandy",27,"Scientist"]]

# file_path = "output.csv"

# try:
#     with open(file_path,"w", newline="") as file:
#         writer = csv.writer(file)
#         for row in employees:
#             writer.writerow(row)
#         print(f"csv file '{file_path}' was created")
# except FileExistsError:
#     print("File already exists, try again")



# #for json
# import json
# employee = {
#     "name": "Spongebob",
#     "age" : 30,
#     "job" : "cook"
# }

# file_path = "output.json"
# try:
#     with open(file= file_path, mode = "w") as file:
#         json.dump(employee,file, indent= 4 )
#         print(f"json file {file_path} was created ")
# except FileExistsError:
#     print("That file already exists")





# #for txt
# txt_data = "I like pizza"

# file_path = "output.txt"
# try:
#     with open(file_path, "w") as file:
#         file.write(txt_data)
#         print("File has been created")
# except FileExistsError:
#     print(f"File '{file_path}' already exists")










#==============================READING FILES ======================== READING FILES ========================
#python reading files (.txt, .json, .csv)
#how to read .txt

file_path = "output.txt"
try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File was not found")
except PermissionError:
    print("You do not have permission to read that file")



#how to read .json
import json

file_path = "output.json"
try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content) # content[] if you want to find smth more specifically, i mean, for keys yk. name, age etc
except FileNotFoundError:
    print("File was not found")
except PermissionError:
    print("You do not have permission to read that file")





import csv

file_path = "output.csv"
try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line) #line[] gives the first column, first name, next ages, job positions, etcetera. If you need need it
except FileNotFoundError:
    print("File was not found")
except PermissionError:
    print("You do not have permission to read that file")