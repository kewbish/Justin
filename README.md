# :robot: Justin - A personalized assistant interface
A minimalist, modern CLI for my personal workflows and interactions.  
Made with Python, March 2020 - current.  
Created by [Kewbish](https://github.com/kewbish).
Released under the [MIT License](https://opensource.org/licenses/MIT).  
Issues are welcome, but please ask to claim an issue before beginning any work if you intend to contribute to this repo. If you'd like to work on a personal fork, feel free to do so without opening anything!

## :memo: Note
Justin was created with my personal workflows in mind, and as such, many of the links and features involved are hyper-personalized.  
I've tried my best to implement for Linux and MacOS, but I can't make any promises. Documentation and features may not be applicable on these platforms.   
This was created for developers and those with knowledge with Python; documentation won't outline every step of install or configuration - you're expected to understand how to configure and where to look for edits.  
However, please do check out the [instructions on creating a config.jstn](#configjstn), and if you're a non-developer (or developer) needing help with installs, open an issue.

## :wrench: Setup
Clone this repository, and download + extract the files.  
Create a `config.jstn` file (see instructions [below](#configjstn)) and replace the file path in `justin\justin.py` in the `def jstn_command()` function.  
```python
def jstn_command():
    p = Path("C:/Users/offic/Downloads/Dev/Justin/files/config.jstn")
```
Run `pip install .` in Terminal / Command Prompt to install the project.  
In the future, when you run `justin` in Terminal, you'll be greeted with Justin's helper interface.
*Coming soon: uploading to PyPI when stable 1.0 is released.*
*If you download with `pip install https://github.com/kewbish/Justin/archive/master.zip` - the file to edit can be usually found at `/usr/lib/[python version]/site-packages/Justin/justin/justin.py` on Linux / MacOS, and `C:\Users\[user]\AppData\Local\Programs\Python\[python version]\Lib\site-packages\justin\justin.py` on Windows. If you're having issues finding the `justin` package, run `python` to open IDLE, then `import sys` and `sys.path` to find your Python path - look there for `site-packages` or `dist-packages`, then for `justin` and `justin.py`.*

### :computer: Command Alias
Alternatively, use `DOSKEY` (Windows) or `alias` (Linux) to set up an alias to the `justin\justin.py` file after downloading these files.  
For example, `doskey justin=python path\to\justin.py %*` (on Windows, set up in target properties).  
Information about these can be found [for Windows](https://superuser.com/a/1517751) and [Linux](https://askubuntu.com/a/17538).  
MacOS users - you may have to create a `.bash_profile` or `.zsh` file in your home directory. Run `sudo nano .bash_profile` or `sudo nano .zsh` in your home directory, and add `alias justin=python path/to/justin.py $*`.  

## :hammer_and_wrench: config.jstn
Justin uses a custom `config.jstn` file. You can place this anywhere, just remember to update the path in the Justin file.  
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
The `[Me] GmailPass` is not required; leave empty if you'd like to manually enter your password. This will prevent your password being stolen and left unencrypted. *In the future, I plan to implement an encryption layer.*

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
