import pyperclip

phrase = input("Clapify this: ")
clippedphrase = phrase.split()
clapped = (" 👏 ").join(clippedphrase)
pyperclip.copy(clapped)
