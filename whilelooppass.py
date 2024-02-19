my_pass = "mypass"
password_test = input("Introduce your password: ")

while my_pass != password_test:
    print('Error. Try Again.')
    password_test = input("Introduce your password: ")
else:
    print("You have successful done your login.")