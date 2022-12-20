import tkinter as tk
from tkinter import *
import sys
from OSL_Lexer import *


'''class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)'''



def insertText(textone):
    if __name__ == '__main__':
        characters = textone
        tokens = imp_lex(characters)
        for token in tokens:
            texttwo.insert(1.0, token)

root = Tk()
root.title("UI")
root.resizable(False, False)
root.geometry('600x380+200+100')

a = StringVar()
textone = Text(width=80, height=10, bg="darkgreen", fg='white', textvariable= a)
textone.pack()
btn = Button(text="Зчитати", command=insertText(textone))
btn.pack()
texttwo = Text(width=80, height=10, bg="darkgreen", fg='white', wrap=WORD)
texttwo.pack()
root.mainloop()
