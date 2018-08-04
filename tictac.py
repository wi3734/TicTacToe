import sys
import random

class Engine():
    def __init__(self):
        self.game = Game()

    def start(self):
        self.game.game_current_status()

class Game():
    def __init__(self): #requires an instance of 'Grid' and 'Referee' and two "User"
        self.grid = Grid()
        self.check = Decider()
        self.user1 = User()
        print("User1: {}".format(self.user1.name))
        self.user2 = User()
        print("User2: {}".format(self.user2.name))

    def game_current_status(self):
        temp = self.decide_who_starts()

        if temp == 1:
            while True:
                self.next_turn(self.user1)
                self.next_turn(self.user2)

        else:
            while True:
                self.next_turn(self.user2)
                self.next_turn(self.user1)

    def decide_who_starts(self):
        temp = random.randint(0,1)
        if temp == 1:
            self.user1.ones_marker = 'X'
            self.user2.ones_marker = 'O'

        else:
            self.user2.ones_marker = 'X'
            self.user1.ones_marker = 'O'

        return temp

    def next_turn(self, user):
        print('\n\n')
        print("{}'s turn".format(user.name))
        print("\n\n")
        self.grid.display_status() #displays the grid
        print("\n\n")

        claimed_number = self.grid.mark_a_grid(user)
        if claimed_number == "Claimed":
            return self.next_turn(user)

        user.items.append(claimed_number)
        self.check.tell_who_won(user, self.grid)

class Grid():
    def __init__(self):
        self.grid = self.make_a_grid()

    def make_a_grid(self): #returns a newly generated grid
        grid = {} #3x3
        for x in range(9): #create nine empty blocks that can be marked
            y = x + 1
            grid[y] = " "
        return grid

    def mark_a_grid(self, user): #mark a grid for a user and return the int value
        temp = user.select_the_block()
        if self.grid[temp] != " ":
            print("It's claimed already!")
            return "Claimed"
        else:
            self.grid[temp] = user.ones_marker

        return temp #return number to users for hoarding for the result check!

    def display_status(self): #display the progress
        print(f"{self.grid[1]} | {self.grid[2]} | {self.grid[3]}")
        print("- | - | -")
        print(f"{self.grid[4]} | {self.grid[5]} | {self.grid[6]}")
        print("- | - | -")
        print(f"{self.grid[7]} | {self.grid[8]} | {self.grid[9]}")

class Decider(): #check the winner
    def tell_who_won(self, user, grid): #check if anyone has won
        winner = [[1, 4, 7], [2, 5, 8], [3, 6, 9], #winning combos
                [1, 2, 3], [4, 5, 6], [7, 8, 9],
                [1, 5, 9], [3, 5, 7]]
        true = 0

        user.items.sort(key=int) #sort the user's list in a numerical order


        for win_combo in winner:
            for element in win_combo:
                if element in user.items:
                    true += 1
                    if true == 3:
                        print(f"{user.name} has won!")
                        sys.exit(1)

            true = 0 #reset it after going through each iteration containing a winning combination

        if not " " in grid.grid.values(): #if no one wins
            print("Draw!")
            sys.exit(1)

class User():
    def __init__(self):
        self.name = input("Type in your name> ")
        self.ones_marker = ''
        self.items = []

    def select_the_block(self): #returns the int value that is associated with a block
        try:
            input1 = int(input("Which block would you choose? "))
        except ValueError:
            print("No String!")
            return self.select_the_block()
        else:
            if input1 > 9 or input1 <= 0: #an integer has to be anything from one to nine
                print("From one to nine only!")
                return self.select_the_block()
            else:
                return input1


tictac = Engine()
tictac.start()
