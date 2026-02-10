import tkinter as tk
import random
from tkinter import messagebox

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        
        # ایجاد فریم برای نمایش و ورودی‌ها
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        # توضیح برای کاربر
        self.info_label = tk.Label(self.frame, text="Enter a number (1 for Rock, 2 for Paper, 3 for Scissors)")
        self.info_label.grid(row=0, column=0, columnspan=3, pady=10)

        # ورودی عدد
        self.input_label = tk.Label(self.frame, text="Your choice:")
        self.input_label.grid(row=1, column=0, pady=5)
        self.input_entry = tk.Entry(self.frame)
        self.input_entry.grid(row=1, column=1, pady=5)

        # دکمه شروع بازی
        self.play_button = tk.Button(self.frame, text="Play", command=self.play_game)
        self.play_button.grid(row=2, column=0, columnspan=3, pady=10)

    def play_game(self):
        try:
            # دریافت انتخاب کاربر از ورودی
            user_choice = int(self.input_entry.get())
            
            # بررسی انتخاب کاربر
            if user_choice not in [1, 2, 3]:
                raise ValueError("Please enter a number between 1 and 3.")
            
            # انتخاب تصادفی کامپیوتر
            computer_choice = random.randint(1, 3)
            
            # چاپ انتخاب‌های کامپیوتر و نتیجه بازی
            result = self.get_result(user_choice, computer_choice)
            
            # نمایش نتیجه به کاربر
            messagebox.showinfo("Game Result", f"Computer chose: {computer_choice}\n{result}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number between 1 and 3.")

    def get_result(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie! You both chose the same."
        elif (user_choice == 1 and computer_choice == 3) or \
             (user_choice == 2 and computer_choice == 1) or \
             (user_choice == 3 and computer_choice == 2):
            return "You win!"
        else:
            return "You lose! Please try again."

# ایجاد پنجره اصلی
if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
