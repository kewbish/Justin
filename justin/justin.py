import sys
from getpass import getpass
from email import message_from_string
from imaplib import IMAP4_SSL
from logging import debug
from datetime import datetime
from os import getenv, system, getcwd
from subprocess import Popen, PIPE
from requests import get
from sys import argv
from webbrowser import open_new
from terminaltables import SingleTable
from justin.platform.platform import System
from justin.config import ConfigManager

try:  # catches OS-specific errors
    from os import startfile
except ImportError:
    pass


class Justin:
    def __init__(self):
        self.cfgmgr = ConfigManager()
        self.config = self.cfgmgr.get_config()
        self.platform = System()
        self.commands = {
            'socials': [self.socials, "Opens fresh social media tabs."],
            'local': [self.local, "Bringing local information to terminal."],
            'news': [self.news, "Prints national news thru NewsAPI."],
            'ghissues': [self.github_issues, "Notes open issues - req. auth."],
            'ghinit': [self.github_init, "Prepares Git repo for use."],
            'dev': [self.dev, "Opens developer software."],
            'emails': [self.email, "Opens unread email."],
            'hginit': [self.hugo_init, "Prepares Hugo site."],
            'changevar': [self.changevar, "Change a variable"]
        }

    def socials(self):
        open_new("https://mail.google.com/mail/u/0")
        open_new("https://discordapp.com/channels/@me")
        open_new("https://app.slack.com/client/TFFEQ2X61/CTUSAU05S")
        open_new("https://www.instagram.com/direct/inbox/")
        open_new("https://reddit.com/r/memes/rising")
        telegram_app = self.config.get('path_to_telegram')
        if self.platform.system() == 'Windows' and telegram_app:
            startfile(r"{}".format(telegram_app))
        elif telegram_app:
            proc = Popen(telegram_app, stdout=PIPE, stderr=PIPE)
            debug(proc.stdout.read(), proc.stderr.read())
        debug("Opened socials.")

    def local(self):
        # FIXME: Requirements : bash is only available in WSL or MINGW. It may not work on standalone Windows
        system("bash -c 'curl wttr.in?0'")
        cw = get("https://coronavirus-tracker-api.herokuapp.com/v2/latest").json()
        cor_table = [["Latest", "World"],
                     ["Cases", cw['latest']['confirmed']],
                     ["Deaths", cw['latest']['deaths']],
                     ["Recoveries", cw['latest']['recovered']]]
        print(SingleTable(cor_table, title="COVID-19 Updates").table)
        system("bash -c 'cal'")
        print("Current time is:")
        print(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        debug("Opened local information.")

    def news(self):
        key = self.config.get('newsapi_token')
        country = self.config.get('country', 'ca')
        news = get(
            f"http://newsapi.org/v2/top-headlines?country={country}&apiKey={key}").json()
        try:
            for a in news["articles"]:
                print(f"⚬ {a['title']} - {a['description']}")
            print("\nNews courtesy of the NewsAPI - https://newsapi.org")
        except (IndexError, KeyError):
            print(f"Couldn't retrieve for country {country}")
        debug("Printed news to terminal.")

    def github_issues(self):
        print("Currently, these are the issues you have open.")
        system("bash -c 'curl -u '{username}' https://api.github.com/issues'"
               .format(username=self.config.get('github_username')))  # TODO: Pretty output
        debug("Opened issues.")

    def github_init(self):
        gh_repo_name = argv[2]
        system("git init")
        # FIXME global
        system(f"git remote add https://github.com/{self.config.get('github_username')}/{gh_repo_name}.git")
        print(f"Setting up at: https://github.com/{self.config.get('github_username')}/{gh_repo_name}.git")
        system("git add . && github")
        debug("Set up repo.")

    def dev(self):
        Popen("{ide}".format(
            ide=self.config.get(
                'name_of_your_IDE',
                'notepad.exe' if self.platform.system() == 'Windows' else 'nano'  # specify default for MacOS also
            )
        ), shell=True)
        Popen("{sh}".format(
            sh=self.config.get(
                'name_of_your_terminal_app',
                'cmd.exe' if self.platform.system() == 'Windows' else 'bash'
            )
        ), shell=True)
        open_new("https://trello.com/b/Znkymw6w/dev")
        debug("Opened developer workflow.")
        sys.exit()

    def email(self):
        em = self.config.get('gmail_email_id')
        # pw = getenv("GMAILPASS")  # FIXME: Never save passwd to env, other softwares too have access to it
        pw = getpass()
        print("")
        mail = IMAP4_SSL('imap.gmail.com')
        try:
            mail.login(em, pw)
            mail.select()
            return_code, data = mail.search(None, 'UnSeen')
            del return_code
            mail_ids = data[0].decode()
            id_list = mail_ids.split()
            first_email_id = int(id_list[0])
            latest_email_id = int(id_list[-1])
            for i in range(latest_email_id, first_email_id, -1):
                typ, data = mail.fetch(str(i), '(RFC822)')
                del typ
                for response_part in data:
                    msg = message_from_string(response_part[1].decode("utf-8"))
                    ef = msg['from']
                    es = msg['subject']
                    print(f"{ef} - {es}")
                if not data:
                    print("Nothing to see!")
        except:
            print("Couldn't log in - check credentials.")
        debug("Parsed and printed email.")

    def hugo_init(self):
        gh_repo_name = argv[2]
        try:
            if self.platform.system() == 'Windows':
                with open("deploy-blog.bat", "w") as x:
                    x.write(
                        """
                        @echo off
                        echo Committing to master.
                        git checkout master
                        git add --all && git commit -m %1
                        git push origin --all
                        echo Deleting old publication.
                        rd /s /q public
                        mkdir public
                        git worktree prune
                        rd /s /q .git/worktrees/public/
                        echo Editing worktree.
                        git worktree add -B gh-pages public origin/gh-pages
                        echo Generating site.
                        hugo --buildFuture
                        cd public && git add --all && git commit -m %1
                        git push origin --all
                        cd ..
                        """)
            else:
                with open("deploy-blog.sh", "w") as x:
                    x.write(
                        """
                        @echo off
                        echo Committing to master.
                        git checkout master
                        git add --all && git commit -m %1
                        git push origin --all
                        echo "Deleting old publication."
                        rm -rf public
                        mkdir public
                        git worktree prune
                        rm -rf .git/worktrees/public/
                        echo "Cleaning up."
                        git worktree add -B gh-pages public upstream/gh-pages
                        rm -rf public/*
                        echo "Publishing site."
                        hugo
                        cd public && git add --all && git commit -m $1
                        git push --all
                        """)
            system(f"hugo new site {getcwd()} && hugo new theme")
            with open("README.md", "w") as x:
                x.write(f"# {gh_repo_name}  \nCreated by Kewbish.")
            if self.platform.system() == 'Windows':
                system("del config.toml")
            else:
                system("rm ./config.toml")
            with open("config.yml", "w") as x:
                x.write(f"""
                baseURL: "/"
                languageCode: "en-us"
                title: "{gh_repo_name}""
                theme: "{gh_repo_name}"
                disableKinds: ["taxonomy", "taxonomyTerm"]
                relativeURLs: true
                """)
            debug("Set up Hugo site.")
        except Exception as e:
            print(f"There was an error setting up your site. ErrorCode : {e}")

    def changevar(self):
        config_item = [x for x in self.config]
        for n, command in enumerate(config_item):
            print(f"[{n+1}] {' '.join(command.split('_'))}")
        try:
            item = int(input("Select the number of the variable you would like to change >>> ").strip())
            self.config[config_item[item-1]] = \
                input(f"Enter the new value for {' '.join(config_item[item-1].split('_'))} >>> ")
            self.cfgmgr.update_config(self.config)
            self.cfgmgr.write_file()
            print("Configuration updated sucessfully!")
        except (ValueError, KeyboardInterrupt, EOFError):
            print("\nPlease enter a valid input\n")

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
               ["dev", "Opens developer software."],
               ["emails", "Opens unread email."],
               ["hginit", "Prepares Hugo site."]]
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
    elif a == "emails":
        email()
    elif a == "hginit":
        hugo_init()
    elif a == "help":
        help()
    else:
        help()
except IndexError:
    print("Error: Usage: justin [program] [options]")
