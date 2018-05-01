import random
file = open("HangmanWords.txt",  "r")
words = []
word = ""
for i in file:
    words.append(i.strip())
word = words[random.randrange(len(words))]
lenght = len(word)
letters = ""
for i in range(lenght):
    letters += "⏚"
print (letters)
tries = 6
while letters != word:
    if tries == 1:
        letters = word
    passes = 0
    print ("TRIES:",  tries)
    usr = input("GUESS:")
    position = []
    while passes < lenght:
        if usr == word[passes]:
            position.append(passes)
        passes += 1
    if len(position) == 0:
        tries -= 1
#    print (position, len(position))
    passes = 0
    while passes < len(position):
        letters = letters[:position[passes]] + word[position[passes]] + letters[position[passes]+1:]
        passes += 1
    print (letters)
