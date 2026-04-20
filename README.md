# Activity 3: Python Mini-Game Platform

A modular, extensible game manager built with Python. This platform allows for dynamic game loading and features a centralized UI for navigation and settings.

## 🚀 Features

- **Dynamic Loading:** Automatically detects and loads any game placed in the `/games` directory using `importlib`.
- **Centralized Pause System:** Standardized Pause/Restart/Exit menus across all games via class inheritance.
- **Grid System:** Custom `Grid` class used for rendering game boards (Wordle) and ASCII art (Hangman).

## 🎮 Included Games

1. **Wordle:** Guess the 5-letter word with color-coded feedback.
2. **Blackjack:** Classic card game logic (Text-based).
3. **Hangman:** Save the man by guessing the word, rendered on a coordinate grid.

## 🛠️ Project Structure

- `main.py`: The entry point and platform manager.
- `grid.py`: Core logic for 2D coordinate management.
- `/games`: Plugin folder for game modules.

## 👥 Credits (Group 3)

- **Developers:** Rei Agustin & Xavier Algenio
- **Buddy Parents:** Euri Barbon & Lara Carillo

## 📝 Instructions

1. Run `python main.py` to start the platform.
2. Navigate using the numeric keys.
3. Type **'pause'** or **'p'** during any game to access the pause menu.
