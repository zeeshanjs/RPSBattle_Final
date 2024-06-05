import tkinter as tk
from tkinter import messagebox
import random
import time
from PIL import Image, ImageTk

CANVAS_WIDTH = 700
CANVAS_HEIGHT = 700  # Increased height to accommodate buttons at the bottom
NUM_ROUNDS = 5

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Battle")

        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()

        self.player_name = "PLAYER"
        self.user_score = 0
        self.computer_score = 0
        self.rounds_played = 0

        self.trophy_image = Image.open("t2.png")
        self.trophy_image = self.trophy_image.resize((100, 100), Image.Resampling.LANCZOS)
        self.trophy_photo = ImageTk.PhotoImage(self.trophy_image)

        self.handshake_image = Image.open("hs2.png")
        self.handshake_image = self.handshake_image.resize((100, 100), Image.Resampling.LANCZOS)
        self.handshake_photo = ImageTk.PhotoImage(self.handshake_image)

        self.splash_image = Image.open("Splash.png")
        self.splash_image = self.splash_image.resize((500, 200), Image.Resampling.LANCZOS)
        self.splash_photo = ImageTk.PhotoImage(self.splash_image)

        self.create_start_screen()

    def create_start_screen(self):
        self.canvas.delete("all")
        self.canvas.create_image(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 3, image=self.splash_photo)
        self.start_button = tk.Button(self.root, text="START GAME", font=('Arial', 12), bg='lightgreen', command=self.start_game)
        self.start_button_window = self.canvas.create_window(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2 + 100, window=self.start_button)

    def start_game(self):
        self.canvas.delete("all")
        self.start_button.destroy()
        self.create_game_screen()
        self.show_game_buttons()

    def create_game_screen(self):
        self.user_choice_label = self.canvas.create_text(CANVAS_WIDTH // 2, 50, text="Your Choice: ", font=('Arial', 16, 'bold'), fill='black')
        self.computer_choice_label = self.canvas.create_text(CANVAS_WIDTH // 2, 100, text="Computer Choice: ", font=('Arial', 16, 'bold'), fill='black')
        self.result_label = self.canvas.create_text(CANVAS_WIDTH // 2, 150, text="Result: ", font=('Arial', 20, 'bold'), fill='black')

        self.user_score_label = self.canvas.create_text(CANVAS_WIDTH // 2 - 100, 200, text="Player Score", font=('Arial', 14), fill='blue')
        self.user_score_value = self.canvas.create_text(CANVAS_WIDTH // 2 - 100, 230, text="0", font=('Arial', 20, 'bold'), fill='blue')

        self.computer_score_label = self.canvas.create_text(CANVAS_WIDTH // 2 + 100, 200, text="Computer Score", font=('Arial', 14), fill='red')
        self.computer_score_value = self.canvas.create_text(CANVAS_WIDTH // 2 + 100, 230, text="0", font=('Arial', 20, 'bold'), fill='red')

        self.rounds_frame = self.canvas.create_rectangle(CANVAS_WIDTH // 2 - 50, 260, CANVAS_WIDTH // 2 + 50, 290, outline='black', width=2, fill='white')
        self.rounds_label = self.canvas.create_text(CANVAS_WIDTH // 2, 275, text=f"Round {self.rounds_played+1}/{NUM_ROUNDS}", font=('Arial', 14, 'bold'))

        self.rock_button = tk.Button(self.root, text="ROCK", font=('Arial', 12), bg='lightblue', command=lambda: self.play_game("Rock"))
        self.paper_button = tk.Button(self.root, text="PAPER", font=('Arial', 12), bg='lightgreen', command=lambda: self.play_game("Paper"))
        self.scissors_button = tk.Button(self.root, text="SCISSORS", font=('Arial', 12), bg='lightcoral', command=lambda: self.play_game("Scissors"))

        self.rock_button_window = self.canvas.create_window(CANVAS_WIDTH // 2 - 150, 575, window=self.rock_button)
        self.paper_button_window = self.canvas.create_window(CANVAS_WIDTH // 2, 575, window=self.paper_button)
        self.scissors_button_window = self.canvas.create_window(CANVAS_WIDTH // 2 + 150, 575, window=self.scissors_button)

    def show_game_buttons(self):
        self.canvas.itemconfig(self.rock_button_window, state='normal')
        self.canvas.itemconfig(self.paper_button_window, state='normal')
        self.canvas.itemconfig(self.scissors_button_window, state='normal')

    def hide_game_buttons(self):
        self.canvas.itemconfig(self.rock_button_window, state='hidden')
        self.canvas.itemconfig(self.paper_button_window, state='hidden')
        self.canvas.itemconfig(self.scissors_button_window, state='hidden')

    def get_computer_choice(self):
        choices = ["Rock", "Paper", "Scissors"]
        return random.choice(choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Draw"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            return "User Wins"
        else:
            return "Computer Wins"

    def play_game(self, user_choice):
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(user_choice, computer_choice)

        if result == "User Wins":
            self.user_score += 1
            result_text = "Result: User Wins!"
            result_color = "blue"
        elif result == "Computer Wins":
            self.computer_score += 1
            result_text = "Result: Computer Wins!"
            result_color = "red"
        else:
            result_text = "Result: It's a Draw!"
            result_color = "purple"

        self.rounds_played += 1

        self.canvas.itemconfig(self.user_choice_label, text=f"Your Choice: {user_choice}", fill="blue")
        self.canvas.itemconfig(self.computer_choice_label, text=f"Computer Choice: {computer_choice}", fill="red")
        self.canvas.itemconfig(self.result_label, text=result_text, fill=result_color)
        self.canvas.itemconfig(self.user_score_value, text=str(self.user_score))
        self.canvas.itemconfig(self.computer_score_value, text=str(self.computer_score))
        self.canvas.itemconfig(self.rounds_label, text=f"Round {self.rounds_played}/{NUM_ROUNDS}")

        if self.rounds_played >= NUM_ROUNDS:
            self.show_final_result()

    def show_final_result(self):
        self.hide_game_buttons()

        if self.user_score > self.computer_score:
            final_result = f"{self.player_name} WINS THE GAME!"
            final_result_color = "blue"
            self.canvas.create_text(CANVAS_WIDTH // 2, 340, text=final_result, font=('Arial', 30, 'bold'), fill=final_result_color)
            self.canvas.after(500, self.draw_trophies, CANVAS_WIDTH // 2, 450)
        elif self.computer_score > self.user_score:
            final_result = "COMPUTER WINS THE GAME!"
            final_result_color = "red"
            self.canvas.create_text(CANVAS_WIDTH // 2, 340, text=final_result, font=('Arial', 30, 'bold'), fill=final_result_color)
            self.canvas.after(500, self.draw_trophies, CANVAS_WIDTH // 2, 450)
        else:
            final_result = "IT'S A TIE!"
            final_result_color = "purple"
            self.canvas.create_text(CANVAS_WIDTH // 2, 340, text=final_result, font=('Arial', 30, 'bold'), fill=final_result_color)
            self.canvas.after(500, self.draw_handshakes, CANVAS_WIDTH // 2, 450)

        self.canvas.after(1000, self.show_restart_button)

    def show_restart_button(self):
        self.restart_button = tk.Button(self.root, text="CLICK TO RESTART", font=('Arial', 14), command=self.restart_game)
        self.restart_button_window = self.canvas.create_window(CANVAS_WIDTH // 2, 600, window=self.restart_button)

    def restart_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.restart_button.destroy()
        self.canvas.delete("all")
        self.create_start_screen()
    def draw_trophies(self, x, y):
        self.trophy = self.canvas.create_image(x, y, image=self.trophy_photo)
        self.wiggle(self.trophy)

    def draw_handshakes(self, x, y):
        self.handshake = self.canvas.create_image(x, y, image=self.handshake_photo)
        self.wiggle(self.handshake)

    def wiggle(self, image):
        for _ in range(10):
            self.canvas.move(image, -5, 0)
            self.canvas.update()
            time.sleep(0.05)
            self.canvas.move(image, 10, 0)
            self.canvas.update()
            time.sleep(0.05)
            self.canvas.move(image, -5, 0)
            self.canvas.update()
            time.sleep(0.05)

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()

