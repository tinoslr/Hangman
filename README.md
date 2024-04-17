# Hangman
This is a python Project. I'm trying to create a Hangman Game

This is my blog about this project:

17.04.2024: Today I got a better understanding of the "Self" argument inside a class. In my Understanding it gives access to the init methode for functions outside of the class.
For example within the main function, root = tk.TK() is now the new  "master" argument inside the init Methode. The class can now change the mainwindow(root) by calling self.master.title for example.
The line "self.master = master' is also important. Otherwise root could get access to the variables inside the init Methode.   
