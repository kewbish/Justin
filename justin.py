from dotenv import load_dotenv
from email import message_from_string
from imaplib import IMAP4_SSL
from logging import debug
from datetime import datetime
from os import getenv, popen, system
from requests import get
from sys import argv
from webbrowser import open_new
from terminaltables import SingleTable
try:
    from os import startfile
    # Linux OSes do not allow opening lnk's
except ImportError:
    startfile = False


def socials():
    open_new("https://mail.google.com/mail/u/0")
    open_new("https://discordapp.com/channels/@me")
    open_new("https://app.slack.com/client/TFFEQ2X61/CTUSAU05S")
    open_new("https://www.instagram.com/direct/inbox/")
    open_new("https://reddit.com/r/memes/rising")
    if startfile:
        # If OS supports startfile
        startfile(r"C:\Users\offic\Downloads\Dev\Tools\Shortcuts\Telegram.lnk")
    debug("Opened socials.")


def local():
    system("bash -c 'curl wttr.in?0'")
    cw = get("https://coronavirus-tracker-api.herokuapp.com/v2/latest").json()
    bc = get(f"https://coronavirus-tracker-api.herokuapp.com/v2/locations?country_code={getenv('JUSTIN_COUNTRY_CODE', 'CA')}").json()
    try:
        cor_table = [["Latest", "World", "BC"],
                     ["Cases", cw['latest']['confirmed'],
                      bc['locations'][0]['latest']['confirmed']],
                     ["Deaths", cw['latest']['deaths'],
                      bc['locations'][0]['latest']['deaths']],
                     ["Recoveries", cw['latest']['recovered'],
                      bc['locations'][0]['latest']['recovered']]]
        print("\n")
        print(SingleTable(cor_table, title="Coronavirus Updates").table)
        print("\n")
    except IndexError:
        print("Couldn't get Coronavirus updates for your country {}".format(getenv('JUSTIN_COUNTRY_CODE')))
    system("bash -c 'cal'")
    print("Current time is:")
    print(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    debug("Opened local information.")


def news():
    load_dotenv(r"C:\Users\offic\Downloads\Dev\Justin\files\.env")
    key = getenv("NEWSAPI")
    news = get(f"http://newsapi.org/v2/top-headlines?country=ca&apiKey={key}").json()
    for a in news["articles"]:
        print(f"⚬ {a['title']} - {a['description']}")
    print("\nNews courtesy of the NewsAPI - https://newsapi.org")
    debug("Printed news to terminal.")


def github_issues():
    print("Currently, these are the issues you have open.")
    p = system("bash -c 'curl -u 'kewbish' https://api.github.com/issues'")
    debug("Opened issues.")


def github_init():
    gh_repo_name = argv[2]
    system("git init")
    system(f"git remote add https://github.com/kewbish/{gh_repo_name}.git")
    print(f"Setting up at: https://github.com/kewbish/{gh_repo_name}.git")
    system("git add . && github")
    debug("Set up repo.")


def dev():
    system("code && cmd")
    open_new("https://trello.com/b/Znkymw6w/dev")
    debug("Opened developer workflow.")


def email():
    load_dotenv(r"C:\Users\offic\Downloads\Dev\Justin\files\.env")
    em = getenv("GMAILUSER")
    pw = getenv("GMAILPASS")
    mail = IMAP4_SSL('imap.gmail.com')
    mail.login(em, pw)
    mail.select()
    return_code, data = mail.search(None, 'UnSeen')
    mail_ids = data[0].decode()
    id_list = mail_ids.split()
    first_email_id = int(id_list[0])
    latest_email_id = int(id_list[-1])
    for i in range(latest_email_id, first_email_id, -1):
        typ, data = mail.fetch(str(i), '(RFC822)')
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = message_from_string(response_part[1].decode("utf-8"))
                ef = msg['from']
                es = msg['subject']
                print(f"{ef} - {es}")
    debug("Parsed and printed email.")


def help():
    print(r"""       _           _   _
      | |         | | (_)
      | |_   _ ___| |_ _ _ __
  _   | | | | / __| __| | '_ \
 | |__| | |_| \__ \ |_| | | | |_
  \____/ \__,_|___/\__|_|_| |_(_)
 """)
    options = [["Program", "What it does"],
               ["socials", "Opens fresh social media tabs."],
               ["local", "Bringing local information to terminal."],
               ["news", "Prints national news thru NewsAPI."],
               ["ghissues", "Notes open issues - req. auth."],
               ["ghinit", "Prepares Git repo for use."],
               ["dev", "Opens developer software."]]
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
    elif a == "news":
        news()
    elif a == "ghissues":
        github_issues()
    elif a == "ghinit":
        github_init()
    elif a == "dev":
        dev()
    elif a == "email":
        email()
    elif a == "help":
        help()
    else:
        help()
except IndexError:
    print("Error: Usage: justin [program] [options]")
