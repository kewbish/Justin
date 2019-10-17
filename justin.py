from os import system

print("Justin is at the ready.")
menuChoice = input("What would you like assistance with? ").lower().strip()
if menuChoice == "newday":
    system("python " +
           "C:\\Users\\offic\\Downloads\\Dev\\Justin\\scripts\\new_day.py")
elif menuChoice == "botherjustin" or menuChoice == "bother":
    system("python " +
           "C:\\Users\\offic\\Downloads\\Dev\\Justin\\scripts\\bother.py")
elif menuChoice == "spamstats" or menuChoice == "spam":
    system("python " +
           "C:\\Users\\offic\\Downloads\\Dev\\Justin\\scripts\\spam_stats.py")
    system("python " +
           "C:\\Users\\offic\\Downloads\\Dev\\Justin\\scripts\\clapify.py")
else:
    print("Ah yes, words. Can't particularly understand that one.")
    exit(0)
