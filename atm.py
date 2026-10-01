
correct_password = "python123"


password = input("Password: ")


while password != correct_password:


    print("Wrong, try again")

    password = input("Password: ")


print("Access granted")