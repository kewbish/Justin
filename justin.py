from os import startfile
from subprocess import call
import tkinter as t
from tkinter import font
import tkinter.ttk as ttk
from webbrowser import open_new


def socials(self):
    open_new("https://mail.google.com/mail/u/0")
    open_new("https://discordapp.com/channels/@me")
    open_new("https://app.slack.com/client/TFFEQ2X61/CTUSAU05S")
    open_new("https://www.instagram.com/direct/inbox/")
    open_new("https://reddit.com/r/memes/rising")
    startfile(r"C:\Users\offic\Downloads\Dev\Tools\Shortcuts\Telegram.lnk")


root = t.Tk()
root.geometry("800x550")
root.title("Justin - Here to help.")
root.configure(background="#1e1e1e")

mb = font.Font(family="Montserrat Bold", size=50)
mbs = font.Font(family="Montserrat Bold", size=40)
ml = font.Font(family="Montserrat Light", size=20)

dash = t.Frame(root)
dash.configure(background="#1e1e1e")
dash.grid(padx=15, pady=10)

header_title = t.Label(root, text="Justin.")
header_title.grid(row=1, column=1)
header_title.configure(font=mb, background="#1e1e1e", fg="white")

header_separate = ttk.Separator(root, orient="vertical")
header_separate.grid(column=2, row=1, sticky="ns", padx=15)

header_search_front = t.Entry(root)
header_search_front.grid(column=3, row=1)
header_search_front.configure(width=25, fg="white", background="#1e1e1e",
                              font=ml, borderwidth=3)

main_frame = t.Frame(root)
main_frame.configure(background="#1e1e1e")
main_frame.grid(columnspan=3, column=1, row=2, pady=10)

main_new_day = t.Button(main_frame, text="Socials.")
main_new_day.configure(background="#252525", fg="white", font=mbs)
main_new_day.grid(column=1, row=1)
main_new_day.bind('<Button-1>', socials)

root.mainloop()
