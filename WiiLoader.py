import urllib.request
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import zipfile
import os,sys
def resource_path(name):
    base = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base, name)
options = ["400cc", "OptPack (Feather)", "Platinum Runner"]
folder_path = ""
def opensdfolder():
    global folder_path
    folder_path = filedialog.askdirectory(title="Select a Folder")
    print(folder_path)

def installfunction():
    if folder_path == "":
        print("Pick an SD folder first!")
        return
    if selected_option.get() == "400cc":
        url = "https://github.com/TheSchmelz2008/database/releases/download/1/400cc.zip"
        urllib.request.urlretrieve(url, "400cc.zip")
        with zipfile.ZipFile("400cc.zip") as z:
            z.extractall(folder_path)
        print("Installed!")
    if selected_option.get() == "Platinum Runner":
        url = "https://github.com/TheSchmelz2008/database/releases/download/1/platinumrunner.zip"
        urllib.request.urlretrieve(url, "platinumrunner.zip")
        with zipfile.ZipFile("platinumrunner.zip") as z:
            z.extractall(folder_path)
        print("Installed!")
    if selected_option.get() == "OptPack (Feather)":
        url = "https://github.com/TheSchmelz2008/database/releases/download/1/optpack.zip"
        urllib.request.urlretrieve(url, "optpack.zip")
        with zipfile.ZipFile("optpack.zip") as z:
            z.extractall(folder_path)
        print("Installed!")
window = Tk()
window.geometry("390x210")
window.title("WiiLoader")
window.config(background='white')
warn = tk.Label(window,text="Note: OptPack will freeze the program but it will install though",font=('Calibri',10),bg='white',fg='black')
warn.place(x=25,y=180)
opensd = Button(window, text="Open SD Folder", fg='white', bg='green',height=2,width=12)
opensd.config(command=opensdfolder)
opensd.place(x=8,y=130)
selected_option = tk.StringVar(window)
selected_option.set("Choose a mod")
dropdown = tk.OptionMenu(window, selected_option, *options)
dropdown.place(x=130,y=135)
install = Button(window,text="Install",fg='white',bg='green',width=12,height=2,command=installfunction)
install.place(x=280,y=130)
icon = PhotoImage(file=resource_path("logo.png"))
window.iconphoto(False, icon)
title = tk.Label(text="WiiLoader",font=('Times New Roman',40),fg='black',bg='white')
title.pack()
window.mainloop()