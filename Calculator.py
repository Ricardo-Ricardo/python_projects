import tkinter

window = tkinter.Tk() # main window
window.minsize(400,400) # size of window in pixels
window.title("Title")    # title of window
window.wm_iconbitmap("icon_name.ico") # set icon

counter = 0 # count each button press

def center(window):
    window.update_idletasks() # redraw widgets

    width = window.winfo_width() 
    height = window.winfo_height()

    x = (window.winfo_screenwidth() // 2) - (width // 2) # calculate geometry
    y = (window.winfo_screenheight() // 2) - (height // 2)

    window.geometry('{}x{}+{}+{}'.format(width, height, x, y)) # set geometry

def press():
    global counter
    counter += 1 # counts the button presses
    label.config(text = f"Button clicked: {counter} times") # set label

center(window)

label = tkinter.Label(window, text = "Click the Button") # set label
label.place(x=10, y=10)

button = tkinter.Button(window, text="Button", command=press) # set the button
button.place(x = 10, y = 40)

window.mainloop() 
