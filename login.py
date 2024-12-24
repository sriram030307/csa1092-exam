def login(username, password):
    correct_username = "admin"
    correct_password = "password123"
    if username == correct_username and password == correct_password:
        return "Login successful!"
    else:
        return "Login failed. Invalid credentials."
if __name__ == "__main__":
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    print(login(user, pwd))
