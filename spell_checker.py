from spellchecker import SpellChecker # here from the "spellchecker" libarary we import the "SpellChecker" class

spell=SpellChecker() # create the spell object to call SpellChecker class 

misspelled_word=spell.unknown(["amerca","fridy","universty","schol","student","houe"]) # "unknown" is the method by which we will get the word not found in dictionary

print(misspelled_word) # printing the missspelled word

for word in misspelled_word: # "for" loop for the iteration of list

    print ("correct word is :",spell.correction(word)) # "correction" is the method in spellchecker to correct misspelled word

    print ("candidate word is :",spell.candidates(word))# "candidates" is the method in spellchecker to give related words
   
    #======= reference ======
    # https://www.youtube.com/watch?v=JE7qXaF806Q&t=941s