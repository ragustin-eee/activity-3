import os
import importlib

# This is the "Blueprint" for all games
class BaseGame:
    def __init__(self, name):
        self.name = name

    def start(self):
        """Override this in the specific game file."""
        print(f"\n--- Starting {self.name} ---")
        print("Type 'pause' at any time to open the Pause Menu.")
        return self.game_loop()

    def game_loop(self):
        raise NotImplementedError("Each game must implement its own game_loop.")

    def pause_menu(self):
        while True:
            print("\n--- PAUSE MENU ---")
            print("1. Resume")
            print("2. Restart")
            print("3. Exit to Main Menu")
            choice = input("Select an option: ")

            if choice == '1': return "RESUME"
            if choice == '2': return "RESTART"
            if choice == '3': return "EXIT"

def load_games():
    game_list = {}
    # Scan the 'games' directory
    for filename in os.listdir('./games'):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3] # Remove '.py'
            module = importlib.import_module(f'games.{module_name}')

            # Assuming each file has a class named 'Game'
            if hasattr(module, 'Game'):
                game_list[module_name.capitalize()] = module.Game()
    return game_list

def main_menu():
    games = load_games()

    while True:
        print("\n============================")
        print("   OFFLINE GAME PLATFORM")
        print("============================")
        print("1. Games Selection")
        print("2. Options/Settings")
        print("3. Exit")

        choice = input("\nAction: ")

        if choice == '1':
            print("\n--- AVAILABLE GAMES ---")
            list_names = list(games.keys())
            for idx, name in enumerate(list_names, 1):
                print(f"{idx}. {name}")

            # Simple selection logic
            g_choice = int(input("Select game number: ")) - 1
            selected_game = games[list_names[g_choice]]
            selected_game.start()

        elif choice == '2':
            print("\n--- SETTINGS & CREDITS ---")
            print("Group: 3")
            print("Members: Rei Agustin & Xavier Algenio (Apps) and Euri Barbon & Lara Carillo (Buddy Parents)")
            print("Instructions: Select a game and follow on-screen prompts.")
            input("\nPress Enter to return...")

        elif choice == '3':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main_menu()