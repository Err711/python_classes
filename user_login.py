# Homework:
# create class User:
# username
# password
# email
# age
# phone
# In a json file store all user information as database
# create class named PyRequest which will be initialised with:
# headers: list, default []
# authorization: True/False, default None
# body: {}, default None
# user: User obj, default None
# class should have method called
# local_login(username, password) : which updates self.user with user if one is found with given credentials if not
# updates with None: You should search for users in json file
# create function get_user_info(request):
# decorate it with login_required decorator:
# the point of decorator is to check weather there is user inside request or not:
# if there is user get_user_info function should return user all information if not should raise an error with message
# “401 Unauthorized request error”
# implementation:
# 1. create PyRequest object.
# 2. ask user to provide username and password with input and call login function
# 3. call get_user_info for the specific request
import json


class User:
    user_list = []
    # def __init__(self, username=input("Username: "), password=input("Password: "), email=input("Email: "),
    #              age=int(input("Age: ")), phone=int(input("Phone number: "))):

    def __init__(self, username, password, email, age, phone):
        self.username = username
        self.password = password
        self.email = email
        self.age = age
        self.phone = phone
        self.user_list.append(self.user_dict())

    def user_dict(self):
        dict_ = {
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "age": self.age,
            "phone": self.phone
        }
        return dict_

    def json_convert(self):
        with open("user_info_db.json", "w") as json_db:
            json.dump(self.user_list, json_db, indent=4)
        return json_db


class PyRequest(User):
    def __init__(self, username, password, email, age, phone):
        super().__init__(username, password, email, age, phone)
        self.name_input = None
        self.pass_input = None
        self.user = None
        self.headers = []
        self.authorization = None
        self.body = None

    def local_login(self):
        self.name_input = input('Username: ')
        self.pass_input = input('Password: ')
        with open("user_info_db.json", "r") as user_login:
            self.user = json.load(user_login)

    def get_user_info(self):
        for i in self.user:
            if self.name_input in i["username"] and self.pass_input in i["password"]:
                self.body = {
                    "username": self.username,
                    "email": self.email,
                    "age": self.age,
                    "phone": self.phone
                }
                return self.body
                # return f"Hi {self.username}!\n" \
                #        f"email: {self.email}\n" \
                #        f"age: {self.age} \n" \
                #        f"phone: {self.phone}"

            else:
                return ValueError(f"Wrong username/password")

    def login_required(self):
        def decorator(func):
            pass


a = PyRequest("name", "pass", "gmail.com", 22, 97)
b = PyRequest("name777", "pass", "mail.ru", 21, 94)
# c = PyRequest(username=input("Username: "), password=input("Password: "), email=input("Email: "),
#               age=int(input("Age: ")), phone=int(input("Phone number: ")))
a.json_convert()
print("login")
a.local_login()
print(a.get_user_info())



