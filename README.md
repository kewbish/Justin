# :robot: Justin - A personalized assistant interface
A minimalist, modern CLI for my personal workflows and interactions.  
Made with Python, March 2020 - current.  
Created by [Kewbish](https://github.com/kewbish).
Released under the [MIT License](https://opensource.org/licenses/MIT).  

## :memo: Note
Justin was created with my personal workflows in mind, and as such, many of the links and features involved are hyper-personalized.  
However, please do check out the [instructions on creating a config.jstn](#configjstn).

## :wrench: Setup
Run `justin.cmd` in Terminal after downloading the files and moving `justin.py` into the `C:\Users\offic\Downloads\Dev\Justin\` folder. Alternatively, edit the `.cmd` file.  
You may need to place a doskey command in the startup properties of your Command Prompt. Instructions to do so can be found [here](https://superuser.com/a/1517751).  
The Linux / Mac version of the DOSKEY command is `alias`. Run `alias justin='python \path\to\file $*'` to setup an alias for Justin.  

## :hammer_and_wrench: config.jstn
Justin uses a custom `config.jstn` file. You can place this anywhere, just remember to update the path in the Justin class.  
The format is as follows:
```
[Socials]
Link1 = "https://google.com"
Link2 = "C:\path\to\shortcut.lnk"

[NewsApi]
Key = 1337c0d3r

[Dev]
IDE = code
TrelloLink = https://trello.com/b/linktoboard/board

[Me]
Country = ca
GitHubUser = username
GmailUser = example@gmail.com
GmailPass = examplePassword
```
The `[Socials]` area can have as many links as you'd like, these are the only keys where the name doesn't matter.  
The `[NewsApi] Key` requires you to set up a key with the [NewsAPI](https://newsapi.org).  
The `[Dev] IDE` will be run in terminal, so make sure an alias is set up to run it.  
The `[Me] Country` is a lowercase ISO two-letter country code.  

## :gear: Implemented Workflows
Workflows:
- `justin socials` - opens social media
- `justin local` - opens local information
- `justin news` - opens top national headlines - thanks [NewsAPI](https://newsapi.org)
- `justin ghissues` - opens currently-open issues assigned to me
- `justin ghinit` - prepares a folder for developing
- `justin dev` - opens developer workflow
- `justin emails` - opens summaries of unread emails
- `justin hginit` - prepares a Hugo site  

## :handshake: Contributors
Thanks to the following for their work!  
- [Srevin Saju](https://github.com/srevinsaju)
