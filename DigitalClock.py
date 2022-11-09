from tkinter import Label, Tk
from PIL import ImageTk, Image
import time

window = Tk()
window.title("Digital Clock - Python")

#We added icon to the window, if you want to add icon to your window, you have to download the icon and save it in the same folder as your python file.
#If you have downloaded the icon, you can uncomment the following line and comment the line after it.
#window.iconbitmap("icon.ico")

icon = Image.open("digitalClock.png")
photo = ImageTk.PhotoImage(icon)
window.wm_iconphoto(False, photo)

#We added background color to the window.
window.geometry("420x150")
window.resizable(False,False)
text_font= ("Helvetica", 68, 'bold')
background = "#f2e750"
foreground= "#363529"
border_width = 25   

label = Label(window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)

digital_clock()
window.mainloop()
