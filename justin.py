from os import system

print("Justin is at the ready.")
menuChoice = input("What would you like assistance with? ").lower().strip()
if menuChoice == "newday":
    system("python scripts/new_day.py")
elif menuChoice == "botherjustin" or menuChoice == "bother":
    system("python scripts/bother_justin")
elif menuChoice == "spamstats" or menuChoice == "spam":
    system("python scripts/spam_stats.py")
elif menuChoice == "clap":
    system("python scripts/clapify.py")
else:
    print("Ah yes, words. Can't particularly understand that one.")
    exit()
