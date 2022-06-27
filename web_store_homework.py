# Homework:
# Suppose that we have a web store,
# and clients that order  smth from store.
# You should create a web store class, and store every address of  order in that web store class.
# The point is that we need to have a class method to see from how many address were ordered the goods,
# and to count how many times the same address ordered something:
# HINT: Every time an order is being created an instance of WebStore is created:
# We need to know top X addresses accessing this web store as well
import json
from pprint import pprint


class WebStore:
    def __init__(self):
        self.game_list = None

    def items(self):
        s = {}
        with open("games_for_web_store.json", "r") as game_list:
            self.game_list = json.load(game_list)
            for i in range(len(self.game_list)):
                s[self.game_list[i]['game_name']] = self.game_list[i]['game_price']
        return s


class Customers:
    def __init__(self, user_choice, user_address):
        self.user_choice = user_choice
        self.user_address = user_address


class Present(WebStore, Customers):
    def __init__(self, user_name):
        super(WebStore).__init__()
        super(Customers).__init__()
        self.user_name = user_name

    def intro(self):

        return f"Hello {self.user_name}!\n" \
               f"Our games: \n{self.items()}"

    def game_choice(self):
        pass

    def email_sending(self):
        pass


a = Present(input(f"Welcome to our GameStore!\n"
                  f"Enter your name please:\n"))
print(a.intro())
# a = Present("name")

b = Present(input("Enter game name: \n"))





