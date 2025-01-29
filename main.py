from tkinter import *
from file import click, sc, clear, bksps, evaluate

root = Tk()
root.title("Scientific Calculator")

entry = Entry(root, width=50, borderwidth=5, relief=RIDGE, fg="White", bg="Black")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=15)

button_width = 8
button_height = 2

buttons = [
    ('lg', 1, 0), ('ln', 1, 1), ('(', 1, 2), (')', 1, 3), ('.', 1, 4),
    ('^', 2, 0), ('deg', 2, 1), ('sin', 2, 2), ('cos', 2, 3), ('tan', 2, 4),
    ('Sqrt', 3, 0), ('C', 3, 1), ('Bksps', 3, 2), ('mod', 3, 3), ('/', 3, 4),
    ('x!', 4, 0), ('7', 4, 1), ('8', 4, 2), ('9', 4, 3), ('*', 4, 4),
    ('1/x', 5, 0), ('4', 5, 1), ('5', 5, 2), ('6', 5, 3), ('-', 5, 4),
    ('pi', 6, 0), ('1', 6, 1), ('2', 6, 2), ('3', 6, 3), ('+', 6, 4),
    ('e', 7, 0), ('0', 7, 1), ('=', 7, 2)
]

for (text, row, col) in buttons:
    bg_color = "grey" if col in {0, 4} else "black"
    fg_color = "black" if col in {0, 4} else "white"
    
    button = Button(root, text=text, width=button_width, height=button_height, bg=bg_color, fg=fg_color, relief=RAISED)
    button.grid(row=row, column=col)
    
    if text in {'sin', 'cos', 'tan', 'lg', 'ln', 'Sqrt', 'x!', '1/x', 'pi', 'e', 'deg'}:
        button.bind("<Button-1>", lambda event, entry=entry: sc(entry, event.widget))
    elif text == "=":
        button.config(command=lambda entry=entry: evaluate(entry))
    elif text == "C":
        button.config(command=lambda entry=entry: clear(entry))
    elif text == "Bksps":
        button.config(command=lambda entry=entry: bksps(entry))
    else:
        button.config(command=lambda t=text, entry=entry: click(entry, t))

root.mainloop()