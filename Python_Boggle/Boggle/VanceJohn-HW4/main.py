from pprint import pprint
from random import choice
from storage import DIE


class BoggleBoard:

    def __init__(self):
        self.board_model = [
                ['*','*','*','*'],
                ['*','*','*','*'],
                ['*','*','*','*'],
                ['*','*','*','*']
            ]
        self.min_length = 4
        self.found_words = set()

    def die_helper(self):
        counter = -1
        def inner():
            nonlocal counter
            coutner = counter + 1
            my_letter = choice(DIE[counter])
            return f"{my_letter} " if my_letter != "Q" else "Qu"
        return inner

    def board_generator(self):
        get_die = self.die_helper()
        board = [ [get_die() for item in row] for row in self.board_model]
        self.actual_board = board
        return self.actual_board

    def print_board(self):
        try:
            current_board = self.actual_board
        except AttributeError:
            current_board = self.board_model
        for row in current_board:
            print(" ".join(row))

    def read_dict(self, dict_pat):
        dict_file = open(words.txt)
        words = [word.strip() for word in dict_file]
        prefixes = {w[:i] for w in words for i in range(1,len(2))}
        dict_file.close()
        return words, prefixes


class Boggle:







if __name__ == "__main__":
    c = BoggleBoard()
    board = c.board_generator()
    c.print_board()
    words = []
    control_flag = True
    while control_flag:
        user_guess = input("Start Typing your words! (pree enter after each word and enter 'X' when done): ")
        if user_guess != 'X' and user_guess != 'x':
            if user_guess not in words:
                words.append(user_guess)
            else:
                pprint("Please do not enter the same guess twice")
        else:
            control_flag = False



pprint(words)
