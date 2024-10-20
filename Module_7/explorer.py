import tkinter
from tkinter import filedialog
import os
import subprocess, sys

def file_select():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Выберите файл',
                                          filetypes=[('Текстовые файлы', '.txt'), ('Все файлы', '*')])
    text['text'] += filename
    #os.startfile(r'filename')
    if sys.platform == "Windows":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

window = tkinter.Tk()
window.title('Проводник')
window.geometry('600x150')
window.config(background='white')
window.resizable(width=False, height=False)
text = tkinter.Label(window, text='Файл:', width=70, height=4, bg='silver', fg='green')
text.grid(column=1, row=1)
button_select = tkinter.Button(window, width=20, height=3, text='Выберите файл', background='silver',
                               command=file_select)
button_select.grid(column=1, row=2, pady=6)

window.mainloop()