import tkinter as tk
import random

class HangmanGame:
    def __init__(self,master):
        self.master = master
        self.master.title("Hangman")
        self.master.geometry("900x600")
        self.word_list = ["python", "lasagna","japan","witcher"]
        self.secret_word = self.choose_secret_word()
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.attempts_left = 7
        self.initialize_gui()
        self.update_hangman_canvas()


    def choose_secret_word(self):
        return random.choice(self.word_list)
    

    def initialize_gui(self):
        self.hangman_canvas = tk.Canvas(self.master ,width=300, height=300, bg="white")
        self.hangman_canvas.pack(pady=20)
        
        self.word_display = tk.Label(self.master, text="_ " * len(self.secret_word), font=("Helvetica",30))
        self.word_display.pack(pady=(40, 20))

        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(pady=20)
        #self.setup_alphabet_buttons()

    def update_hangman_canvas(self):
        self.hangman_canvas.delete("all")
        incorrect_guess_count = len(self.incorrect_guesses)
        if incorrect_guess_count >= 1:
            self.hangman_canvas.create_line(50,180,150,180)



def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
    

if __name__ == "__main__":
    main()