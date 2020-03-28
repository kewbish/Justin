from configparser import ConfigParser
from datetime import datetime
from email import message_from_bytes
from imaplib import IMAP4_SSL
from json import loads
from logging import debug
from os import system, getcwd
from requests import get
from sys import argv
from terminaltables import SingleTable
from webbrowser import open_new

posix = False
try:
    from os import startfile
except ImportError:
    posix = True


class Justin:
    def __init__(self, path_to_config):
        config = ConfigParser()
        config.read(path_to_config)
        self.socials_links = config.items("Socials")
        self.news_api_key = config.get("NewsApi", "Key")
        self.country = config.get("Me", "Country")
        self.github_user = config.get("Me", "GitHubUser")
        self.ide = config.get("Dev", "IDE")
        self.trello_link = config.get("Dev", "TrelloLink")
        self.gmail_user = config.get("Me", "GmailUser")
        self.gmail_pass = config.get("Me", "GmailPass")

    def runner(self, arg):
        method = arg
        mtr = getattr(self, method, lambda: help)
        return mtr()

    def socials(self):
        for key, sl in self.socials_links:
            if not sl.endswith(".lnk"):
                open_new(f"{sl}")
            elif not posix and sl.endswith(".lnk"):
                startfile(f"{sl}")
            del key
        debug("Opened socials.")

    def local(self):
        system("bash -c 'curl wttr.in?0'")
        system("bash -c 'cal'")
        print("Current time is:")
        print(datetime.now().strftime("%d %B %Y, %H:%M:%S"))
        debug("Opened local information.")

    def news(self):
        key = self.news_api_key
        ctry = self.country
        news = get(
            f"http://newsapi.org/v2/top-headlines?country={ctry}&apiKey={key}"
        ).json()
        try:
            for a in news["articles"]:
                print(f"⚬ {a['title']} - {a['description']}")
            print("\nNews courtesy of the NewsAPI - https://newsapi.org")
        except (IndexError, KeyError):
            print(f"Couldn't retrieve for country {ctry}.")
        debug("Printed news to terminal.")

    def ghissues(self):
        usr = self.github_user
        print("Please log in to view open issues.")
        system(f"bash -c 'curl -u '{usr}' https://api.github.com/issues'")
        debug("Opened issues.")

    def ghinit(self):
        usr = self.github_user
        try:
            gh_repo = argv[2]
            system("git init")
            system(f"git remote add https://github.com/{usr}/{gh_repo}.git")
            print(f"Setting up at: https://github.com/{usr}/{gh_repo}.git")
            system("git add . && github")
            debug("Set up repo.")
        except IndexError:
            print("Please provide a GitHub repo.")

    def dev(self):
        system(f"{self.ide}")
        open_new(f"{self.trello_link}")
        debug("Opened developer workflow.")

    def emails(self):
        em = self.gmail_user
        pw = self.gmail_pass
        mail = IMAP4_SSL("imap.gmail.com")
        mail.login(em, pw)
        mail.select("inbox")
        typ, data = mail.search(None, "UNSEEN")
        del typ
        for x in reversed(data[0].split()):
            ty, dat = mail.fetch(x, "(RFC822)")
            mess = message_from_bytes(dat[0][1])
            print(f"{mess.get('from')} - {mess.get('subject')}")
            del ty
        mail.close()
        mail.logout()
        debug("Parsed and printed email.")

    def hginit(self):
        try:
            gh_repo = argv[2]
            if not posix:
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
                        """
                    )
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
                        """
                    )
            system(f"hugo new site {getcwd()} && hugo new theme")
            with open("README.md", "w") as x:
                x.write(f"# {gh_repo}  \nCreated by Kewbish.")
            if not posix:
                system("del config.toml")
            else:
                system("rm ./config.toml")
            with open("config.yml", "w") as x:
                x.write(
                    f"""
                baseURL: "/"
                languageCode: "en-us"
                title: "{gh_repo}""
                theme: "{gh_repo}"
                disableKinds: ["taxonomy", "taxonomyTerm"]
                relativeURLs: true
                """
                )
            debug("Set up Hugo site.")
        except IndexError:
            print("There was an error, please check GitHub repo provided.")

    def internet(self):
        system("bash -c 'curl http://ipecho.net/plain'")
        system("bash -c 'speedtest-cli --simple'")
        debug("Checked internet options.")

    def help(self):
        print(
            r"""             _           _   _
            | |         | | (_)
            | |_   _ ___| |_ _ _ __
        _   | | | | / __| __| | '_ \
       | |__| | |_| \__ \ |_| | | | |_
        \____/ \__,_|___/\__|_|_| |_(_)
    """
        )
        options = [
            ["Program", "What it does"],
            ["socials", "Opens fresh social media tabs."],
            ["local", "Bringing local information to terminal."],
            ["news", "Prints national news thru NewsAPI."],
            ["ghissues", "Notes open issues - req. auth."],
            ["ghinit", "Prepares Git repo for use. - req. GH repo name"],
            ["dev", "Opens developer software."],
            ["emails", "Opens unread email."],
            ["hginit", "Prepares Hugo site.- req. GH repo name"],
            ["internet", "Prints IP and checks speed."],
        ]
        print(SingleTable(options, title="Here to help.").table)
        print("Usage: justin [program] [options]")

    def justin_command(self):
        if len(argv) == 2:
            a = argv[1]
        elif len(argv) == 1:
            a = "help"
        justin = Justin(r"C:\Users\offic\Downloads\Dev\Justin\files\config.jstn")
        justin.runner(a)


if __name__ == "__main__":
    if len(argv) == 2:
        a = argv[1]
    elif len(argv) == 1:
        a = "help"
    justin = Justin(r"C:\Users\offic\Downloads\Dev\Justin\files\config.jstn")
    justin.runner(a)
