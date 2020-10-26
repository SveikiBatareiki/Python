# 3. Apgrieztie vārdi
# Lietotājs ievada teikumu.
# Izvadam visus teikuma vārdus apgrieztā formā.
# Alus kauss -> Sula ssuak
# PS Te varētu noderēt split un join operācijas.

sentence = input("Please input sentence")
words = sentence.split()#dividing in words - list
reverse_words = words
reverse_words.reverse()
joined_reversed_sentence = " ".join(words)
print(sentence, "->", joined_reversed_sentence.capitalize())