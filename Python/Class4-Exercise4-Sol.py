import random

mylist = []
i = 1
while i < 6:
    print("Enter number", i, ": ", end='')
    try:
        mylist.append(int(input()))
        i +=1
    except:
        print("Value must be integer!")

print('Your list:')
for x in mylist:
    print(x, end=' ')  # printing without new line use end = ''

mylist.sort(reverse = True)

print('\nYour sorted list:')

for x in mylist:
    print(x, end=' ')

Random_Message = '\nYour random element is: {}'
random_element = random.choices(mylist, k=1) # Use choices to print random element
random_element_new = str(random_element).split("[")[1].split("]")[0] # Why?

print(Random_Message.format(random_element)) 
print(Random_Message.format(random_element_new))

mylist.remove(int(random_element_new))
print('\nYour list after deleting '+ str(random_element_new) +' element:')
for x in mylist:
    print(x, end=' ')