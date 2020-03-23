# Justin - A personalized assistant dashboard
A minimalist, modern CLI for my personal workflows and interactions.  
Made with Python and Tkinter, March 2020 - current.  
Released under the [GPLv3 License](https://www.gnu.org/licenses/gpl-3.0.en.html).  
## Setup
Run `justin.cmd` in Terminal after downloading the files and moving `justin.py` into the `C:\Users\offic\Downloads\Dev\Justin\` folder. Alternatively, edit the `.cmd` file.  
You may need to place a doskey command in the startup properties of your Command Prompt. Instructions to do so can be found [here](https://superuser.com/a/1517751).  
The Linux / Mac version of the DOSKEY command is `alias`. Run `alias justin='python \path\to\file $*'` to setup an alias for Justin.  
## Workflows and Features
Workflows:
- `justin socials` - opens social media
- `justin local` - opens local information
- `justin news` - opens top national headlines - thanks [NewsAPI](https://newsapi.org)
- `justin ghissues` - opens currently-open issues assigned to me
- `justin ghinit` - prepares a folder for developing
- `justin dev` - opens developer workflow
- `justin emails` - opens summaries of unread emails
Features:
- Infrastructure to support infinite workflows and commands
- Pretty ASCII!
