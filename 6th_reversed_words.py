# 3. Apgrieztie vārdi
# Lietotājs ievada teikumu.
# Izvadam visus teikuma vārdus apgrieztā formā.
# Alus kauss -> Sula ssuak
# PS Te varētu noderēt split un join operācijas.

sentence = input("Please input sentence")
reverse_words = sentence[::-1]
reverse_words = reverse_words.split()#dividing in words - list
reverse_words = " ". join(reverse_words)
#print(len(reverse_words))
#or item in reverse_words:
#    reverse_words[item] = reversed(reverse_words[item])
print(sentence, "->", reverse_words.capitalize())
