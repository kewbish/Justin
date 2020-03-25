# :robot: Justin - A personalized assistant interface
A minimalist, modern CLI for my personal workflows and interactions.  
Made with Python, March 2020 - current.  
Released under the [MIT License](https://opensource.org/licenses/MIT).  

## :memo: Note
Justin was created with my personal workflows in mind, and as such, many of the links and features involved are hyper-personalized. If you'd like to use this project, go right ahead (I'll even upload this to PyPi if usage is high) but beware: you'll have to spend the time to customize and rewrite some things for yourself, such as:  
- File paths, especially for shortcuts and environment variables
- Links to websites that you frequent
- MacOS / Linux support
- Little tweaks to commands (I like to run Hugo with `--buildFuture` on, for example)

## :wrench: Setup
Run `justin.cmd` in Terminal after downloading the files and moving `justin.py` into the `C:\Users\offic\Downloads\Dev\Justin\` folder. Alternatively, edit the `.cmd` file.  
You may need to place a doskey command in the startup properties of your Command Prompt. Instructions to do so can be found [here](https://superuser.com/a/1517751).  
The Linux / Mac version of the DOSKEY command is `alias`. Run `alias justin='python \path\to\file $*'` to setup an alias for Justin.  

## :gear: Workflows and Features
Workflows:
- `justin socials` - opens social media
- `justin local` - opens local information
- `justin news` - opens top national headlines - thanks [NewsAPI](https://newsapi.org)
- `justin ghissues` - opens currently-open issues assigned to me
- `justin ghinit` - prepares a folder for developing
- `justin dev` - opens developer workflow
- `justin emails` - opens summaries of unread emails
- `justin hginit` - prepares a Hugo site  

Features:
- Infrastructure to support infinite workflows and commands
- Pretty ASCII!
