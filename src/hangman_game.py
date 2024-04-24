import tkinter as tk
import random

class HangmanGame:
    def __init__(self,master):

        # basic configuration of the window 
        self.master = master
        self.master.title("Hangman")
        self.master.geometry("900x650")
        self.master.config(bg ="grey")

        # basic configs of the game itself
        # enter a set of words which can be guessed. Must be CAPITAL letters
        self.word_list = ["PYTHON", "LASAGNA","JAPAN","WITCHER"]
        self.secret_word = self.choose_secret_word()

        # 2 sets for correct guesses and incorrect guesses
        self.correct_guesses = set()
        self.incorrect_guesses = set()

        # dont change this value. game still playable but doesnt corresponde to hangman canvas
        self.attempts_left = 7

        #function to initialzie the hangman canvas and the buttons frame 
        self.initialize_gui()

        self.update_hangman_canvas()


    def choose_secret_word(self):
    
        return random.choice(self.word_list)
    

    def initialize_gui(self):

        # create a canvas in the main window for the hangman image
        self.hangman_canvas = tk.Canvas(self.master ,width=300, height=300, bg="light grey", highlightbackground="grey" )
        # show the image in the window. without the pack function it wouldnt show up
        self.hangman_canvas.pack(pady=20)
        
        # create this _____ thing where the letters are shown 
        self.word_display = tk.Label(self.master, text="_ " * len(self.secret_word), font=("Helvetica",30), bg="grey")
        self.word_display.pack(pady=(40, 20))

        # create the big frame where the buttons are put
        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(pady=20)
        self.setup_alphabet_buttons()

        # create a reset button 
        self.reset_button = tk.Button(self.master, text = "Reset Game" , command=self.reset_game)
        self.reset_button.pack(pady=(10,0))


    def setup_alphabet_buttons(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        

        upper_row = alphabet[:13]
        lower_row = alphabet[13:]

        # devide the buttons in two groups. one half will be put in the upper frame and the others in the lower frame. 
        upper_frame = tk.Frame(self.buttons_frame, bg="grey")
        upper_frame.pack()

        lower_frame = tk.Frame(self.buttons_frame, bg = "grey")
        lower_frame.pack()

        # create a button for each letter in the upper row. each button has a implemented function guess_letter()
        for letter in upper_row:
            button = tk.Button(upper_frame, text = letter, command=lambda l=letter: self.guess_letter(l), width=4, height=2, bg = "light grey")
            button.pack(side="left", padx=2, pady=2)

        for letter in lower_row:
            button = tk.Button(lower_frame, text=letter, command=lambda l=letter: self.guess_letter(l), width=4, height=2, bg ="light grey")
            button.pack(side="left", padx=2, pady=2)

    def update_hangman_canvas(self):

        # reset the hangman image each round 
        self.hangman_canvas.delete("all")

        stages = [self.draw_head, self.draw_body, self.draw_left_arm, self.draw_right_arm, self.draw_left_leg, self.draw_right_leg, self.draw_face]

        # number of incorrect guesses equals the stage which should be added.
        for i in range(len(self.incorrect_guesses)):
            if i < len(stages):
                stages[i]()
    
    def draw_head(self):
      self.hangman_canvas.create_oval(125, 50, 185, 110, outline="black")

    def draw_body(self):
        self.hangman_canvas.create_line(155, 110, 155, 170, fill="black")

    def draw_left_arm(self):
        self.hangman_canvas.create_line(155, 130, 125, 150, fill="black")

    def draw_right_arm(self):
        self.hangman_canvas.create_line(155, 130, 185, 150, fill="black")

    def draw_left_leg(self):
        self.hangman_canvas.create_line(155, 170, 125, 200, fill="black")

    def draw_right_leg(self):
        self.hangman_canvas.create_line(155, 170, 185, 200, fill="black")

    def draw_face(self):
        self.hangman_canvas.create_line(140, 70, 150, 80, fill="black") # Left eye
        self.hangman_canvas.create_line(160, 70, 170, 80, fill="black") # Right eye
        self.hangman_canvas.create_arc(140, 85, 170, 105, start=0, extent=-180, fill="black")
    

    def guess_letter(self,letter):

        # compare the letter which was given by the button with the secret choosen word. if the guess is not already in  the guessed words set, add it there. If its not in secret word it was a wrong guess.
        # Add it to this set and reduce the attempts by one. Call the update_hangman_canvas function so the image gets updated.
        if letter in self.secret_word and letter not in self.correct_guesses:
            self.correct_guesses.add(letter)
        elif letter not in self.incorrect_guesses:
            self.incorrect_guesses.add(letter)
            self.attempts_left -= 1
            self.update_hangman_canvas()
        

        self.update_display()
        self.check_game_over()

    def update_display(self):
        # update the screen. Iterate through the secret word and check if this letter exists in the correct_guesses set. If so join the letter in the var displayed_word.
        displayed_word = " ".join(letter if letter in self.correct_guesses else "_" for letter in self.secret_word)

        #reconfig the word_display with the new found information
        self.word_display.config(text=displayed_word)
    
    def check_game_over(self):

        # if every letter of the secret word is within the correcr guesses set, you should have guessed the correct word
        if set(self.secret_word).issubset(self.correct_guesses):
            self.display_game_over_message("Congratulations. You have won")
        elif self.attempts_left == 0:
            self.display_game_over_message(f"You have lost. The word was: {self.secret_word}")

    def display_game_over_message(self,message):

        # when the game is over the reset button and the letter buttons should disappear
        self.reset_button.pack_forget()
        self.buttons_frame.pack_forget()

        # a label should appear with the correct message 
        self.game_over_label = tk.Label(self.master, text = message, font=("Helvetica", 18), fg="red", bg="grey")
        self.game_over_label.pack(pady=(10, 20))

        # new reset button
        self.restart_button = tk.Button(self.master, text="Restart Game", command=self.reset_game, width=20, height=2)
        self.reset_button.pack(pady=(10, 20))


    def reset_game(self):

        #reset the var and lists
        self.secret_word = self.choose_secret_word()
        self.correct_guesses = set()
        self.incorrect_guesses= set()
        self.attempts_left = 7

        
        self.hangman_canvas.delete("all")
        self.update_display()

        for frame in self.buttons_frame.winfo_children():
            for button in frame.winfo_children():
                button.configure(state=tk.NORMAL)
 
        self.reset_button.pack(pady=(10, 0))
     
        if hasattr(self, 'game_over_label') and self.game_over_label.winfo_exists():
          self.game_over_label.pack_forget()
        if hasattr(self, 'restart_button') and self.restart_button.winfo_exists():
          self.restart_button.pack_forget()

        self.buttons_frame.pack()


def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
    

if __name__ == "__main__":
    main()