from tkinter import *
import pyshorteners

def convert():
    s = pyshorteners.Shortener().tinyurl.short(url.get())
    shorturl.set(s)
root = Tk()
root.title(" URL Shortner")
root.geometry("400x350")
root.resizable(False, False)
root.config(background="#ffffe0")

url = StringVar()
shorturl = StringVar()

Label(root, text="URL Shortner", bg="#ffff00", fg="#E74C3C", font="verdana 22 ").place(x=80, y=10)
Label(root, text="*************************************", bg="#ffffe0", fg="#E74C3C"
            , font="verdana 12 ").place(x=15, y=50)

Label(root, text="Enter URL Here ", bg="#2C3E50", fg="#EAECEE", font="verdana 10 bold"
            , padx=2, pady=4).place(x=10, y=100)
Entry(root, textvariable=url, font="verdana 12", width=30).place(x=7, y=120)

Button(root, text="Convert...", bg="#fdde6c", fg="#000", font="verdana 12 "
        , command=convert, relief=GROOVE).place(x=7, y=180)

Label(root, text="Shortened URL - Copy & Paste in browser", bg="#2C3E50", fg="#EAECEE"
            , font="verdana 10 bold", padx=2, pady=2).place(x=7, y=250)
Entry(root, textvariable=shorturl, width=35, font="verdana 12").place(x=7, y=270)

root.mainloop()