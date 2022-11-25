import os 
import sys
from time import time
from pytube import YouTube, exceptions
from tkinter import *
from customtkinter import *

#Initialize all the settings
set_appearance_mode("dark") #Set the appearance mode to dark, Set it to "light" for light mode, and "system" for system default
set_default_color_theme("blue") 

for i in os.listdir(os.getcwd()): #Check if the folder "Downloads" exists
    if i == "Youtube_Downloads":
        print("Folder exists")
    elif os.path.exists("Youtube_Downloads") == False:
        os.mkdir("Youtube_Downloads") #If not, create it
    
#Downloaded video function
def download_video(entryLink):
    try:
        startTime=time()
        downloadLocation="Youtube_Downloads"
        YouTube(entryLink).streams.get_highest_resolution().download(downloadLocation)
        endTime=time()

        #Showing the download time in new window
        infoPopup=CTk()
        infoPopup.title("Download Status")
        infoPopup.geometry("250x100")
        infoPopup.resizable(False, False)
        infoPopup.grid_columnconfigure(0, weight=1)
        infoPopup.grid_rowconfigure((0,1), weight=1)
        msg = StringVar()#Message variable
        msg.set(f"Download successful!\nTotal time taken: {round(endTime-startTime,3)} seconds")
        label=CTkLabel(infoPopup, text=msg.get())
        label.grid(row=0, column=0, sticky="nsew")
        infoButton=CTkButton(infoPopup, text="OK", command=infoPopup.destroy)
        infoButton.grid(row=1, column=0, sticky="nsew")
        infoPopup.mainloop()

    except exceptions.RegexMatchError:
        errorPopup=CTk()
        errorPopup.title("Error")
        errorPopup.geometry("300x100")
        errorPopup.resizable(False, False)
        errorPopup.grid_columnconfigure(0, weight=1)
        errorPopup.grid_rowconfigure((0,1), weight=1)
        error_label = CTkLabel(errorPopup, text="Please enter a valid YouTube link")
        error_label.grid(row=0, column=0, sticky="nsew")
        infoButton = CTkButton(errorPopup, text="OK", command=errorPopup.destroy)
        infoButton.grid(row=1, column=0)
        errorPopup.mainloop()

#initialize the main window
window = CTk()
window.title("Youtube Video Downloader")
window.geometry("500x300")
window.resizable(False, False)
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure((0,1,2), weight=1)
CTkLabel(window, text="Enter the YouTube link below").grid(row=0, column=0, sticky="nsew")
entryLink = CTkEntry(window)   
entryLink.grid(row=1, column=0, sticky="nsew")
CTkButton(window, text="Download", command=lambda: download_video(entryLink.get())).grid(row=2, column=0, sticky="nsew")
window.mainloop()

