#program to validate login credentials
#concept - if else statements to check username and password

user_input_username = input("Enter the username: ")
user_input_password = input("Enter the password: ")
username_val = ("newbeetoveteran")
password_val = ("123456@abc")


if user_input_username == username_val and user_input_password == password_val:
    print("Login Successful!")

else:
    print("Incorrect credentials entered. Please check your details and enter again.")