import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.configure(bg="green")
        self.root.geometry("400x400")

        
        self.user_score = 0
        self.computer_score = 0

        
        self.instructions_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Helvetica", 14))
        self.instructions_label.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 18, "bold"))
        self.result_label.pack(pady=20)

        
        self.rock_button = tk.Button(root, text="Rock", width=10, font=("Helvetica", 12), command=lambda: self.user_choice("rock"))
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(root, text="Paper", width=10, font=("Helvetica", 12), command=lambda: self.user_choice("paper"))
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(root, text="Scissors", width=10, font=("Helvetica", 12), command=lambda: self.user_choice("scissors"))
        self.scissors_button.pack(pady=5)

        
        self.score_label = tk.Label(root, text="User: 0  Computer: 0", font=("Helvetica", 12))
        self.score_label.pack(pady=20)


        self.play_again_button = tk.Button(root, text="Play Again", font=("Helvetica", 12), command=self.reset_game, state=tk.DISABLED)
        self.play_again_button.pack(pady=10)

    def user_choice(self, choice):
        
        self.rock_button.config(state=tk.DISABLED)
        self.paper_button.config(state=tk.DISABLED)
        self.scissors_button.config(state=tk.DISABLED)

        
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)

        
        if choice == computer_choice:
            result = "It's a Tie!"
        elif (choice == 'rock' and computer_choice == 'scissors') or \
             (choice == 'paper' and computer_choice == 'rock') or \
             (choice == 'scissors' and computer_choice == 'paper'):
            result = "You Win!"
            self.user_score += 1
        else:
            result = "You Lose!"
            self.computer_score += 1

        
        self.result_label.config(text=f"Your Choice: {choice.capitalize()}   Computer's Choice: {computer_choice.capitalize()}\n{result}")

        
        self.score_label.config(text=f"User: {self.user_score}  Computer: {self.computer_score}")

        
        self.play_again_button.config(state=tk.NORMAL)

    def reset_game(self):
        
        self.result_label.config(text="")
        self.rock_button.config(state=tk.NORMAL)
        self.paper_button.config(state=tk.NORMAL)
        self.scissors_button.config(state=tk.NORMAL)
        self.play_again_button.config(state=tk.DISABLED)


root = tk.Tk()
app = RockPaperScissorsGame(root)
root.mainloop()
