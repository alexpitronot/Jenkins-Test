import random
from flask import Flask
app = Flask(__name__)

@app.route("/")

def home():

 fName=input("Enter Your First Name: ")
 lName=input("Enter Your Last Name: ")
 age=input("Enter Your age: ")
 id_n=input("Enter Your ID: ")

 Hello_Message = 'Hello {} {}, {} years old, with ID number: {}.<br> My suggestion for username is \
 <div style="background-color: navy; color: white; font-size: 1.5em; display: unset;"> {}</div>'

 username= str(fName[0]+lName[0]+age+id_n[-3:]+"-"+str(random.randrange(1,10000))).lower()

 return(Hello_Message.format(fName,lName,age,id_n,username))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)