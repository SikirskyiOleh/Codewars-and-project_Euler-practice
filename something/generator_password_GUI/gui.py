import random
import tkinter
from chars import chars

main_window = tkinter.Tk()
main_window.title("Password Generator")
main_window.geometry('500x300')
padd = 50
main_window['padx'] = padd

chk1 = tkinter.IntVar()
chk2 = tkinter.IntVar()
chk3 = tkinter.IntVar()


def password_generate(length):
    password = "".join(random.sample(chars, length))
    display_result.delete(0, tkinter.END)
    display_result.insert(0, password)


def checkbox_check():
    if chk1.get() == 8:
        password_generate(8)
    elif chk2.get() == 12:
        password_generate(12)
    elif chk3.get() == 16:
        password_generate(16)
    else:
        password_generate(8)


title_text = tkinter.Label(text='Password Generator')
title_text.grid(row=0, column=0)
display_result = tkinter.Entry()

display_result.grid(row=1, column=0)
chkone = tkinter.Checkbutton(text='8 Character', onvalue=8, offvalue=0, variable=chk1)
chkone.grid(row=2, column=0)
chktwo = tkinter.Checkbutton(text='12 Character', onvalue=12, offvalue=0, variable=chk2)
chktwo.grid(row=3, column=0)
chkthree = tkinter.Checkbutton(text='16 Character', onvalue=16, offvalue=0, variable=chk3)
chkthree.grid(row=4, column=0)

pass_generate = tkinter.Button(text='Generate', command=checkbox_check)
pass_generate.grid(row=5, column=0)
main_window.mainloop()
