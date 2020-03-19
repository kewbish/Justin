from logging import debug
from os import startfile
from requests import get
from subprocess import call
from sys import argv
from webbrowser import open_new
from terminaltables import SingleTable


def socials():
    open_new("https://mail.google.com/mail/u/0")
    open_new("https://discordapp.com/channels/@me")
    open_new("https://app.slack.com/client/TFFEQ2X61/CTUSAU05S")
    open_new("https://www.instagram.com/direct/inbox/")
    open_new("https://reddit.com/r/memes/rising")
    startfile(r"C:\Users\offic\Downloads\Dev\Tools\Shortcuts\Telegram.lnk")
    debug("Opened socials.")


def local():
    call("bash -c 'curl wttr.in'")
    cw = get("https://coronavirus-tracker-api.herokuapp.com/v2/latest").json()
    bc = get("https://coronavirus-tracker-api.herokuapp.com/v2/locations?country_code=CA").json()
    cor_table = [["Latest", "World", "BC"],
                 ["Cases", cw['latest']['confirmed'],
                 bc['locations'][0]['latest']['confirmed']],
                 ["Deaths", cw['latest']['deaths'],
                 bc['locations'][0]['latest']['deaths']],
                 ["Recoveries", cw['latest']['recovered'],
                 bc['locations'][0]['latest']['recovered']]]
    print(SingleTable(cor_table, title="Coronavirus Updates").table)
    call("bash -c 'cal'")
    print("Current time is:")
    call("time /t")
    debug("Opened local information.")


def help():
    print(r"""       _           _   _
        | |         | | (_)
        | |_   _ ___| |_ _ _ __
    _   | | | | / __| __| | '_ \
    | |__| | |_| \__ \ |_| | | | |_
    \____/ \__,_|___/\__|_|_| |_(_)\n""")
    options = [["Program", "What it does"],
               ["socials", "Opens fresh social media tabs."],
               ["local", "Bringing local information to terminal."]]
    print(SingleTable(options, title="Here to help.").table)
    print("Usage: justin [program] [options]")


try:
    if len(argv) == 1:
        a = "help"
    else:
        a = argv[1].lower()
        args = argv[2:]
    if a == "socials":
        socials()
    elif a == "local":
        local()
    elif a == "help":
        help()
    else:
        help()
except IndexError:
    print("Error: Usage: justin [program] [options]")
