# Uzrakstīt programmu teksta simbola atpazīšanai
# Lietotājs(pirmais spēlētājs) ievada tekstu.
# Tiek izvadītas tikai zvaigznītes burtu vietā. Pieņemsim, ka cipari nebūs, bet atstarpes gan var būt
# Lietotājs(tātad otrs spēlētājs) ievada simbolu. 
# Ja burts ir tad tas burts attiecīgajās vietās tiek parādīts, visi pārējie burti paliek par zvaigznītēm.
# Kartupeļu lauks -> ********* *****
# Ievada a -> *a****** *a***
# Principā tas ir labs iesākums karātavu spēlei.

guessWord = input(str("Please enter text"))
i = 0
hiddenWord = guessWord
#str(hiddenWord)
for i in range(len(guessWord)):
    if guessWord[i] != " ":
        hiddenWord = hiddenWord.replace(guessWord[i], "*")

print(hiddenWord)

letter = input(str("Please input letter!"))
newHiddenWord = ""
for i in guessWord:
    if i ==" ":
        newHiddenWord += " "
    elif i == letter:
        newHiddenWord += letter
    else:
        newHiddenWord +="*"
print(newHiddenWord)

#  while True:
#     try:
#         i = 0
#         hiddenWord.index('*')
#         letter = input(str("Please input letter!"))
#         if guessWord.index(letter) > 0:
#             for i in range(len(guessWord)):
#                 if guessWord[i] == letter:
#                     hiddenWord = hiddenWord.replace(hiddenWord[i], guessWord[i])
#         else:
#             print("This text doesn't contain this letter")
#         print(hiddenWord)       
#     except ValueError:
#         print("You have guessed the sentence/word!")
#         break
#     print("Good job!")