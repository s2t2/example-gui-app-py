from IPython import embed
import tkinter

#
# INITIALIZE A NEW GUI WINDOW
#

window = tkinter.Tk()

#
# INITIALIZE SOME COMPONENTS
#

# MESSAGE

my_message = tkinter.Message(text="Hi. Welcome to my Example GUI Application!", width=1000)

# ENTRY WITH LABEL

entry_value = tkinter.StringVar()

my_label = tkinter.Label(text="Input something here:")
my_entry = tkinter.Entry(textvariable=entry_value)

# BUTTON

def handle_button_click():
    print("NICE. YOU CLICKED THE BUTTON")
    print("THE ENTRY'S INPUT VALUE IS:", my_entry.get())

my_button = tkinter.Button(text="Click Me", command=handle_button_click)














# CHECKBUTTONS ... https://www.tutorialspoint.com/python/tk_checkbutton.htm

# LISTBOX ... https://www.tutorialspoint.com/python/tk_listbox.htm

# RADIO BUTTONS ... https://www.tutorialspoint.com/python/tk_radiobutton.htm

#
# BIND THE INDIVIDUAL COMPONENTS TO THE GUI WINDOW (PACK)
# ... THEN LAUNCH THE GUI WINDOW (MAINLOOP)
#

my_message.pack()

my_label.pack() #my_label.pack(side=tkinter.LEFT)
my_entry.pack() #my_entry.pack(side=tkinter.RIGHT)

my_button.pack()

window.mainloop()
