# 1-Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed
# correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place
# is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user
# guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout the game
# and tell the user at the end.
# The implementation should be based on classes and objects
# 2-Create Triangle class which will have 4 attributes (sides and the height), and methods for calculating the area,
# perimeter, validation of the triangle, and a method to compare the triangle with other one (Note: this method should
# check if the Triangles are alike or not).

# 1.

from random import randint


class Game:
    RANDOM_NUMBER = randint(1000, 9999)
    RANDOM_NUMBER = str(RANDOM_NUMBER)

    def __init__(self, user_number: str):
        self.user_number = user_number
        self.bulls = 0
        self.cows = 0

    def num_check(self):
        if len(self.user_number) != 4:
            raise ValueError("You can enter only 4 digit numbers!")

    def game_check(self):
        if self.user_number == self.RANDOM_NUMBER:
            print("Congrats")
        for i, j in zip(self.RANDOM_NUMBER, self.user_number):
            if i == j:
                self.cows += 1
            else:
                self.bulls += 1
        if self.user_number == "exit":
            print("Game over")

    def present(self):
        return f"Cows {self.cows}\nBulls {self.bulls}\n{self.RANDOM_NUMBER}, {self.user_number}"

# not finished
#     def game_start_stop(self):
#         start = True
#         while start:
#
#             if self.cows != 4:
#                 print(f"Cows {self.cows}\nBulls {self.bulls}")
#                 input()
#             if self.user_number == "exit":
#                 print("Game over")
#                 start = False


# user = Game("4567")  # Game(input("Enter your 4 digit number, 'exit' for exit:\n"))
user = Game(input("Enter your 4 digit number, 'exit' for exit:\n"))
print(user.num_check())
print(user.game_check())
print(user.present())
# print(user.game_start_stop())

