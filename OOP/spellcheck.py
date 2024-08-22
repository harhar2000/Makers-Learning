# Write a program checking spelling of words in a given string and highlights misspelled words
#  by surrounding them with special characters. 

from spellchecker import SpellChecker as spc

class SpellCheck:
    def __init__(self, language='en'):
        self.spell_checker = spc(language=language)

    def check(self, str):
        words = str.split()
        new_str = []

        for word in words:
            if word.lower() in self.spell_checker:
               new_str.append(word)
            else:
                new_str.append(f" -->{word}<-- ")
        new_str = ' '.join(new_str)
        print(new_str)
        
spell_checker = SpellCheck()
spell_checker.check("These words are spnelt correclty")
# => "These words are ~spnelt~ ~correclty~"