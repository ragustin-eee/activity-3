from main import BaseGame
from grid import Grid
import random

class Game(BaseGame):
    def __init__(self):
        super().__init__("Hangman")
        self.word_bank = ["PYTHON", "GITHUB", "SYSTEM", "MATRIX", "BINARY"]
        self.target_word = random.choice(self.word_bank)
        self.guessed_letters = []
        self.lives = 6
        # Use a 5x5 grid to draw the hangman
        self.canvas = Grid(5, 5)

    def update_canvas(self):
        self.canvas.clear_board()
        # Basic gallows (static)
        self.canvas.set_cell(0, 1, "|")
        self.canvas.set_cell(1, 1, "|")

        # Add parts based on lives lost
        if self.lives <= 5: self.canvas.set_cell(1, 2, "O") # Head
        if self.lives <= 4: self.canvas.set_cell(2, 2, "|") # Body
        if self.lives <= 3: self.canvas.set_cell(2, 1, "-") # Left Arm
        if self.lives <= 2: self.canvas.set_cell(2, 3, "-") # Right Arm
        if self.lives <= 1: self.canvas.set_cell(3, 1, "/") # Left Leg
        if self.lives <= 0: self.canvas.set_cell(3, 3, "\\") # Right Leg

    def display(self):
        self.update_canvas()
        for row in self.canvas.grid:
            print(" ".join(row))

        display_word = [char if char in self.guessed_letters else "_" for char in self.target_word]
        print(f"\nWord: {' '.join(display_word)}")
        print(f"Lives: {self.lives} | Guessed: {', '.join(self.guessed_letters)}")

    def game_loop(self):
        while self.lives > 0:
            self.display()
            guess = input("\nGuess a letter (or 'pause'): ").upper()

            if guess == "PAUSE":
                action = self.pause_menu()
                if action == "EXIT": return
                if action == "RESTART": break # Breaks to outer loop
                continue

            if len(guess) != 1 or not guess.isalpha():
                continue

            if guess in self.guessed_letters:
                print("Already guessed!")
                continue

            self.guessed_letters.append(guess)

            if guess not in self.target_word:
                self.lives -= 1

            if all(char in self.guessed_letters for char in self.target_word):
                print(f"Winner! The word was {self.target_word}")
                break

        if self.lives == 0:
            self.display()
            print(f"Game Over! The word was {self.target_word}")
        input("Press Enter...")