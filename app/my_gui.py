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

# RADIO BUTTONS

my_radio_label = tkinter.Label(text="Please selection one of the following options:")
my_radio_value = tkinter.StringVar()
my_radio_a = tkinter.Radiobutton(text="Option A", value="A", variable=my_radio_value)
my_radio_b = tkinter.Radiobutton(text="Option B", value="B", variable=my_radio_value)
my_radio_c = tkinter.Radiobutton(text="Option C", value="C", variable=my_radio_value)

# CHECKBUTTONS

my_checkbox_group_label = tkinter.Label(text="Please check one or more of the following boxes:")
my_checkbox_a_val = tkinter.StringVar()
my_checkbox_a = tkinter.Checkbutton(text="Box A", variable=my_checkbox_a_val)
my_checkbox_b_val = tkinter.StringVar()
my_checkbox_b = tkinter.Checkbutton(text="Box B", variable=my_checkbox_b_val)
my_checkbox_c_val = tkinter.StringVar()
my_checkbox_c = tkinter.Checkbutton(text="Box C", variable=my_checkbox_c_val)

# BUTTON

def handle_button_click():
    print("------------------------------")
    print("NICE. YOU CLICKED THE BUTTON")
    print("THE ENTRY'S INPUT VALUE IS:", my_entry.get())
    print("THE SELECTED RADIO BUTTON'S VALUE IS:", my_radio_value.get())
    print("THE CHECKBOX ON/OFF VALUES FOR A, B, C, RESPECTIVELY, ARE:", [my_checkbox_a_val.get(), my_checkbox_b_val.get(), my_checkbox_c_val.get()])

my_button = tkinter.Button(text="Click Me", command=handle_button_click)

# LISTBOX ... https://www.tutorialspoint.com/python/tk_listbox.htm


#
# BIND THE INDIVIDUAL COMPONENTS TO THE GUI WINDOW (PACK)
# ... THEN LAUNCH THE GUI WINDOW (MAINLOOP)
#

my_message.pack()

my_label.pack() #my_label.pack(side=tkinter.LEFT)
my_entry.pack() #my_entry.pack(side=tkinter.RIGHT)

my_radio_label.pack()
my_radio_a.pack()
my_radio_b.pack()
my_radio_b.pack()

my_checkbox_group_label.pack()
my_checkbox_a.pack()
my_checkbox_b.pack()
my_checkbox_c.pack()

my_button.pack()

window.mainloop()
