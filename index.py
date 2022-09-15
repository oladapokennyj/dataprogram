print("welcome to the official page for inec portal")
user_name = input("input your user_name>")
print(user_name)
password = input("input your password>")
print("welcome", user_name)
print("kindly fill-in the below form")
state = input("state of origin>")
localgov = input ("local goverment>")
age= int(input("enter your age>"))
if age >=19:
    print("you are eligible to vote ")
else:
    print("you are not eligible to vote you dumb fool")
if age<19:
    print("come back in the next", 19-(age),"year")
