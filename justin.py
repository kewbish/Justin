import tkinter as t
from tkinter import font
import tkinter.ttk as ttk
from webbrowser import open_new


def open_url(url):
    open_new(url)


root = t.Tk()
root.geometry("800x550")
root.title("Justin - Here to help.")
root.configure(background="#1e1e1e")

montserrat_bold = font.Font(family="Montserrat Bold", size=50)
montserrat_light = font.Font(family="Montserrat Light", size=20)
underline = font.Font(family="Montserrat Light", size=20)
underline.configure(underline=True)

dash = t.Frame(root)
dash.configure(background="#1e1e1e")
dash.grid(padx=15, pady=10)

header_title = t.Label(root, text="Justin.")
header_title.grid(row=1, column=1)
header_title.configure(font=montserrat_bold, background="#1e1e1e", fg="white")

header_separate = ttk.Separator(root, orient="vertical")
header_separate.grid(column=2, row=1, sticky="ns", padx=15)

header_quicklinks = t.Frame(root)
header_quicklinks.grid(column=3, row=1)

header_quicklinks_gmail = t.Label(header_quicklinks, text="Gmail")
header_quicklinks_gmail.configure(font=underline, background="#1e1e1e",
                                  fg="white")
header_quicklinks_gmail.pack()
header_quicklinks_gmail.bind("<Button-1>", lambda e: open_url(
    "https://mail.google.com"))

root.mainloop()
