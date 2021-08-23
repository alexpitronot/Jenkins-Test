import random
file1 = open("data.txt","a") # use "a" to append data to existing file

fName = input("Enter Your First Name: ")
lName = input("Enter Your Last Name: ")
age = input("Enter Your age: ")
id_n = input("Enter Your ID: ")

Hello_Message = 'Hello {} {}, {} years old, with ID number: {}.\n My suggestion for username is {}'

username = str(fName[0]+lName[0]+age+id_n[-3:]+"-" +
str(random.randrange(1, 10000))).lower()

print(Hello_Message.format(fName, lName, age, id_n, username))

file1.write(Hello_Message.format(fName, lName, age, id_n, username))
file1.close()