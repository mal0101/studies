from tkinter import *

window = Tk()
window.title("Information")
window.geometry('350x200')
window.minsize(350, 200)
label = Label(window, text="Hello World", font=("Arial Bold", 50), bg='red', fg='white')
label.pack()
buttom = Button(window, text="Quit", command=window.quit)
buttom.pack()
# use window.iconbitmap('path') to set the icon of the window
# use window.config to set the background color of the window
window.config(bg='blue')
window.mainloop()