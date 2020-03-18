from os import startfile
from subprocess import call
from webbrowser import open_new
from terminaltables import SingleTable


def socials(self):
    open_new("https://mail.google.com/mail/u/0")
    open_new("https://discordapp.com/channels/@me")
    open_new("https://app.slack.com/client/TFFEQ2X61/CTUSAU05S")
    open_new("https://www.instagram.com/direct/inbox/")
    open_new("https://reddit.com/r/memes/rising")
    startfile(r"C:\Users\offic\Downloads\Dev\Tools\Shortcuts\Telegram.lnk")


def vancouver(self):
    call("bash -c 'curl wttr.in'")


print("""       _           _   _         
      | |         | | (_)        
      | |_   _ ___| |_ _ _ __    
  _   | | | | / __| __| | '_ \   
 | |__| | |_| \__ \ |_| | | | |_ 
  \____/ \__,_|___/\__|_|_| |_(_)""")
options = [["Program", "What it does"], ["Socials", "Opens fresh social media."]]
print(SingleTable(options, title="Here to help.").table)
