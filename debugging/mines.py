#!/usr/bin/python3
import random
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        # Initialize game settings: grid size and number of mines
        self.width = width
        self.height = height
        self.mines_count = mines
        self.mines = set(random.sample(range(width * height), mines))  # Randomly place mines
        self.field = [[' ' for _ in range(width)] for _ in range(height)]  # Game board
        self.revealed = [[False for _ in range(width)] for _ in range(height)]  # Revealed cells
        self.start_time = None  # Timer start time
        self.revealed_count = 0  # Count of revealed cells

    def print_board(self, reveal=False):
        # Function to print the game board
        clear_screen()
        print(f"Mines Left: {self.mines_count - self.revealed_count}")  # Show remaining mines
        print(f"Time: {int(time.time() - self.start_time)} seconds" if self.start_time else "Time: 0 seconds")
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')  # Show mine
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        # Count number of mines around a given cell
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        # Reveal a cell, if it's a mine, return False (game over), else True
        if (y * self.width + x) in self.mines:
            return False
        self.revealed[y][x] = True
        self.revealed_count += 1
        if self.count_mines_nearby(x, y) == 0:
            # If no mines around, recursively reveal neighboring cells
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def choose_difficulty(self):
        # Choose difficulty level (easy, medium, hard)
        print("Choose a difficulty level:")
        print("1. Easy (5x5 grid, 10 mines)")
        print("2. Medium (10x10 grid, 20 mines)")
        print("3. Hard (15x15 grid, 40 mines)")
        choice = int(input("Enter choice (1/2/3): "))
        if choice == 1:
            self.width, self.height, self.mines_count = 5, 5, 10
        elif choice == 2:
            self.width, self.height, self.mines_count = 10, 10, 20
        elif choice == 3:
            self.width, self.height, self.mines_count = 15, 15, 40

    def play(self):
        # Main function to play the game
        self.choose_difficulty()  # Let the player choose difficulty
        self.start_time = time.time()  # Start the timer
        while True:
            self.print_board()  # Print the board on each iteration
            try:
                user_input = input("Enter x coordinate (or 'q' to quit): ")
                if user_input.lower() == 'q':
                    print("You chose to quit the game. Goodbye!")
                    break

                x = int(user_input)  # Get the x-coordinate from user
                y = int(input("Enter y coordinate: "))  # Get the y-coordinate from user

                if not self.reveal(x, y):  # Reveal the selected cell
                    self.print_board(reveal=True)  # Show all mines
                    print("Game Over! You hit a mine.")
                    break

                if self.revealed_count == self.width * self.height - self.mines_count:
                    # Check if all non-mine cells are revealed (Victory Condition)
                    self.print_board(reveal=True)
                    print(f"Congratulations! You've won the game in {int(time.time() - self.start_time)} seconds.")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")

    def restart_game(self):
        # Ask user if they want to restart the game
        restart = input("Do you want to play again? (y/n): ")
        if restart.lower() == 'y':
            self.__init__(width=10, height=10, mines=10)  # Reinitialize game with default settings
            self.play()

if __name__ == "__main__":
    game = Minesweeper()  # Create a new game instance
    game.play()  # Start the game
    game.restart_game()  # Option to restart the game after finishing
