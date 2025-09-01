username=input("enter a username: ")
password=input("enter a password: ")
if username=="admin" and password=="password123":
    print("Login successful")
elif username!="admin":
    print("Error: Invalid username")
elif password!="password123":
    print("Error: Invalid password.") 
