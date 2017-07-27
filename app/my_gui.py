from IPython import embed
import tkinter

def handle_button_click():
    print("NICE. YOU CLICKED THE BUTTON")

#
# INITIALIZE A NEW GUI WINDOW
#

window = tkinter.Tk()

#
# INITIALIZE SOME COMPONENTS
#

# MESSAGE ... https://www.tutorialspoint.com/python/tk_message.htm

# ENTRY ... https://www.tutorialspoint.com/python/tk_entry.htm

# BUTTONS ... https://www.tutorialspoint.com/python/tk_button.htm

my_button = tkinter.Button(text="Click Me", command=handle_button_click)

# CHECKBUTTONS ... https://www.tutorialspoint.com/python/tk_checkbutton.htm

# LISTBOX ... https://www.tutorialspoint.com/python/tk_listbox.htm

# RADIO BUTTONS ... https://www.tutorialspoint.com/python/tk_radiobutton.htm

#
# BIND THE INDIVIDUAL COMPONENTS TO THE GUI WINDOW (PACK)
# ... THEN LAUNCH THE GUI WINDOW (MAINLOOP)
#

my_button.pack()

window.mainloop()
