from IPython import embed
import tkinter

#
# INITIALIZE A NEW GUI WINDOW
#

window = tkinter.Tk()

#
# INITIALIZE SOME COMPONENTS
#

# ENTRY ... https://www.tutorialspoint.com/python/tk_entry.htm

my_label = tkinter.Label(text="Input something here:")
entry_value = tkinter.StringVar()
my_entry = tkinter.Entry(textvariable=entry_value)

# BUTTONS ... https://www.tutorialspoint.com/python/tk_button.htm

def handle_button_click():
    print("NICE. YOU CLICKED THE BUTTON")
    print("THE ENTRY'S INPUT VALUE IS:", my_entry.get())

my_button = tkinter.Button(text="Click Me", command=handle_button_click)












# MESSAGE ... https://www.tutorialspoint.com/python/tk_message.htm


# CHECKBUTTONS ... https://www.tutorialspoint.com/python/tk_checkbutton.htm

# LISTBOX ... https://www.tutorialspoint.com/python/tk_listbox.htm

# RADIO BUTTONS ... https://www.tutorialspoint.com/python/tk_radiobutton.htm

#
# BIND THE INDIVIDUAL COMPONENTS TO THE GUI WINDOW (PACK)
# ... THEN LAUNCH THE GUI WINDOW (MAINLOOP)
#

my_label.pack(side=tkinter.LEFT)
my_entry.pack(side=tkinter.RIGHT)
my_button.pack()

window.mainloop()
