# :robot: Justin - A personalized assistant interface
A minimalist, modern CLI for my personal workflows and interactions.  
Made with Python, March 2020 - current.  
Created by [Kewbish](https://github.com/kewbish).
Released under the [MIT License](https://opensource.org/licenses/MIT).  

## :memo: Note
Justin was created with my personal workflows in mind, and as such, many of the links and features involved are hyper-personalized.  
However, please do check out the [instructions on creating a config.jstn](#configjstn).

## :wrench: Setup
Clone this repository, and download + extract the files.  
Create a `config.jstn` file (see instructions [below](#configjstn)) and replace the file path in `justin\justin.py` in the `def jstn_command()` function.  
```python
def jstn_command():
    path = r"path\to\config.jstn"
```
Run `pip install .` in Terminal / Command Prompt to install the project.  
In the future, when you run `justin` in Terminal, you'll be greeted with Justin's helper interface.
*Coming soon: uploading to PyPI when stable 1.0 is released.*
*If you download with `pip install https://github.com/kewbish/Justin/archive/master.zip` - the file to edit can be found at `/usr/lib/[python version]/site-packages/Justin/justin/justin.py` on Linux / MacOS, and `C:\Users\[user]\AppData\Local\Programs\Python\[python version]\Lib\site-packages\justin\justin.py` on Windows.*

### :computer: Command Alias
Alternatively, use `DOSKEY` (Windows) or `alias` (Linux / MacOS) to set up an alias to the `justin\justin.py` file.  
For example, `doskey justin=python path\to\justin.py %*` (on Windows, set up in target properties).  
Information about these can be found [for Windows](https://superuser.com/a/1517751) and [Linux / MacOS](https://askubuntu.com/a/17538).  

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
- `justin ghinit repo_name` - prepares a folder for developing, takes a GitHub repo name as a parameter
- `justin dev` - opens developer workflow
- `justin emails` - opens summaries of unread emails
- `justin hginit repo_name` - prepares a Hugo site, takes a GitHub repo name as a parameter  
- `justin internet` - prints IP and checks internet speed

## :handshake: Contributors
Thanks to the following for their work!  
- [Srevin Saju](https://github.com/srevinsaju)
