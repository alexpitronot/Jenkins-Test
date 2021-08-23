myarray = ["Alex","David","Moshe","Maria","Maria"]
username = input("What is Your name? ")
myarray.append(username.split(",")[1].strip())
i = 0


y ="MaRIa"
if y.upper() in myarray:
    print("yes")