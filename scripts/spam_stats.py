from pyperclip import paste
from terminaltables import AsciiTable
from operator import itemgetter
from re import sub

no = {'no', 'n', 'nah', 'nope', 'noppers'}
print("Welcome to the Department of Spam Stats.\n" +
      "Have you copied your spam yet?")
choice = input().lower()
if choice in no:
    spam = input("Enter copied phrase here.")
else:
    spam = paste()
chars = []
words = set(spam.split(' '))
for char in spam[::]:
    if char not in chars:
        chars.append(char)
numoccurences = [['# / Times', 'Letter']]
for letter in chars[::]:
    lettercount = spam.count(letter)
    numoccurences.append([str(lettercount), letter])
letter = AsciiTable(sorted(numoccurences, key=itemgetter(0)))
specials = sub(r'[@_!#$%^&*()<>?/\|}{~:]', '', spam)
print("Overall, this spam contains " + str(len(spam)) + " letters and " +
      str(len(spam.split(' '))) + " words.")
print("This spam contains " + str(len(chars)) + " unique characters and " +
      str(len(words)) + " unique words.")
print("The most often occurring letter, " + numoccurences[1][0] +
      " accounts for " + str(int(numoccurences[1][0])/len(spam)) +
      " of the spam.")
print("This spam likely took about " + str((len(spam)/200)) +
      " minutes to type mindfully, and " + str((len(spam)/814)) +
      " minutes to type mindlessly, and would have taken " +
      str((len(spam)/25)) + " minutes to speak.")
print("The factor of ebicspecial of this spam is " +
      str(len(specials)/len(spam)) + ".")
print(letter.table)
