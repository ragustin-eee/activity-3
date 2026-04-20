import random
from main import BaseGame
from grid import Grid

class Game(BaseGame):
    def __init__(self):
        super().__init__("Wordle")
        self.words = ["APPLE", "BEACH", "BRAIN", "CLOUD", "DANCE"]
        self.target_word = random.choice(self.words)
        self.board = Grid(6, 5)
        self.attempts = 0

    def display_board(self):
        print("\n--- WORDLE ---")
        for row in self.board.grid:
            print(f"| {' | '.join(row)} |")
        print("--------------")

    def game_loop(self):
        while self.attempts < 6:
            self.display_board()
            guess = input(f"Guess ({self.attempts+1}/6): ").upper()

            if guess == "PAUSE":
                action = self.pause_menu()
                if action == "EXIT": return
                if action == "RESTART": break # Breaks to outer loop to reset
                continue

            if len(guess) != 5: continue

            feedback = []
            for i in range(5):
                if guess[i] == self.target_word[i]:
                    feedback.append(f"[{guess[i]}]") # Correct spot
                elif guess[i] in self.target_word:
                    feedback.append(f"({guess[i]})") # Wrong spot
                else:
                    feedback.append(f" {guess[i]} ") # Not in word

            for i, val in enumerate(feedback):
                self.board.set_cell(self.attempts, i, val)

            if guess == self.target_word:
                self.display_board()
                print("YOU GOT IT!")
                break

            self.attempts += 1

        input("\nGame over. Press Enter...")