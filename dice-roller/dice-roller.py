import tkinter as tk


dice = {0 : '🎲', 1 : '⚀', 2 : '⚁', 3 : '⚂', 4 : '⚃', 5 : '⚄', 6 : '⚅', }

root = tk.Tk()

root.title('Dice Roller')

root.iconbitmap(r'dice.ico')

root['background'] = 'black'

diceframe = tk.Frame(root)


dice_roll  = tk.Label(diceframe, text = dice[0], font = ('', 200), bg = 'black', fg = 'white').grid(row=0, column=0)

def roll_dice():
    from random import randint
    dice_roll  = tk.Label(diceframe, text = dice[randint(1,6)], font = ('', 200), bg = 'black', fg = 'white', width= 2).grid(row=0, column=0)

diceframe.pack(padx=50)

roll_button = tk.Button(root, text = 'Roll', command = roll_dice, font = ('Baloo Da',14), width = 10, height = 1).pack(padx=10, pady=10)


root.mainloop()