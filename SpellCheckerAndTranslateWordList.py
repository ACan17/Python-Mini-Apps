from spellchecker import SpellChecker
from translate import Translator

spell = SpellChecker()
translator = Translator(to_lang="tr")

word = input("Enter a word: ")
print("True spelling is: " + spell.correction(word))

wordList = spell.candidates(word)

while True:
    print("Possible spellings are: ", wordList)
    print("Do you want to translate it? (y/n)")
    answer = input()
    if answer == "y":
        for i in wordList:
            print(i + " - " + translator.translate(i))
    break