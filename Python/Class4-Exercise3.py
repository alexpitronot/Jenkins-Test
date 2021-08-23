import random

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))
num5 = int(input("Enter number 5: "))

mylist = [num1,num2,num3,num4,num5]

print('Your list:')
print(mylist[0], end = ' ') # printing without new line use end = ''
print(mylist[1], end = ' ') 
print(mylist[2], end = ' ')
print(mylist[3], end = ' ')
print(mylist[4], end = ' ')

mylist.sort(reverse = True)

print('\nYour sorted list:')
print(mylist[0], mylist[1], mylist[2], mylist[3], mylist[4],)

random_num = random.randrange(0,5)

Random_Message = '\nYour random element is: {}'

print(Random_Message.format(mylist[random_num]))

deleted_element = mylist[random_num] # save deleted element
del mylist[random_num]

print('\nYour list after deleting '+ str(deleted_element) +' element:')
print(mylist[0], end = ' ')
print(mylist[1], end = ' ') 
print(mylist[2], end = ' ')
print(mylist[3], end = ' ')