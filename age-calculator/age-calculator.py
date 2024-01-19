import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title('Age Calculator')
root.iconbitmap(r'calculator.ico')
root['background'] = 'black'


def calculate_age():
    try:
        date_of_birth = datetime(day=int(entry1.get()), month=int(entry2.get()), year=int(entry3.get()))
        age = datetime.now() - date_of_birth    
    except:
        error = tk.Label(frame2, text='Wrong Date of Birth input', font = ('Death Hector', 12), bg = 'black', fg = 'white' ).grid(row=0, column=0, sticky='WE')
    else:
        return age                     

def total():
    total_days = calculate_age().days

    years = total_days // 365
    months = (total_days % 365) // 30
    days = (total_days % 365) % 30

    total_age = tk.Label(frame2, text=f'You are here for {years} years, {months} months, {days} days.', font = ('Death Hector', 10), bg = 'black', fg = 'white' ).grid(row=0, column=0, sticky='WE')


def find_days():
    total_days = calculate_age().days

    total_age = tk.Label(frame2, text=f'You are here for {total_days} days.', font = ('Death Hector', 10), bg = 'black', fg = 'white' ).grid(row=0, column=0, sticky='WE')


def find_seconds():
    total_seconds = round(calculate_age().total_seconds(), 2)

    total_seconds = tk.Label(frame2, text=f'You lived for {total_seconds} seconds.', font = ('Death Hector', 10), bg = 'black', fg = 'white' ).grid(row=0, column=0, sticky='WE')




text1 = tk.Label(root, text = 'Date of Birth', font = ('Death Hector', 14), bg = 'black', fg = 'white').pack(padx=20, pady=10)

frame = tk.Frame(root)

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)
frame.columnconfigure(4, weight=1)
frame.columnconfigure(5, weight=1)


text1 = tk.Label(frame, text = 'Day: ', font = ('Death Hector', 12), bg = 'black', fg = 'white').grid(row = 0, column=0, sticky='WE')
entry1 = tk.Entry(frame, width=2, font = ('Death Hector', 12), bg = '#363636', fg = 'white')
entry1.grid(row=0, column=1, sticky='WE')

text2 = tk.Label(frame, text = '  Month: ', font = ('Death Hector', 12), bg = 'black', fg = 'white').grid(row = 0, column=2, sticky='WE')
entry2 = tk.Entry(frame, width=2, font = ('Death Hector', 12), bg = '#363636', fg = 'white')
entry2.grid(row=0, column=3, sticky='WE')

text3 = tk.Label(frame, text = '  Year: ', font = ('Death Hector', 12), bg = 'black', fg = 'white').grid(row = 0, column=4, sticky='WE')
entry3 = tk.Entry(frame, width=4, font = ('Death Hector', 12), bg = '#363636', fg = 'white')
entry3.grid(row=0, column=5, sticky='WE')



frame.pack(padx=10, pady=30, fill='x')

frame1 = tk.Frame(root, borderwidth=2)

frame1.columnconfigure(0, weight=1)
frame1.columnconfigure(1, weight=1)
frame1.columnconfigure(2, weight=1)

btn1 = tk.Button(frame1, text='Calculate\nAge', command= total, font = ('Death Hector', 10)).grid(row=0, column=0, sticky='WE')
btn1 = tk.Button(frame1, text='Calculate\nIn Days', command= find_days, font = ('Death Hector', 10)).grid(row=0, column=1, sticky='WE')
btn1 = tk.Button(frame1, text='Calculate\nIn Seconds', command= find_seconds, font = ('Death Hector', 10)).grid(row=0, column=2, sticky='WE')

frame1.pack(padx=20, pady=20, fill='x')

frame2 = tk.Frame(root)
frame2.pack(padx=20, pady=20, fill='x')




root.mainloop()
