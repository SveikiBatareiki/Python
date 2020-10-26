# 2. Palindroms
# uzrakstiet funkciju is_palindrome(text)
# kas atgriež bool True vai False atkarībā vai vārds vai teikums ir lasāms vienādi no abām pusēm.
# PS no sākuma varat sākt ar viena vārda risinājumu, bet pilns risinājums ignorēs atstarpes(whitespace) un lielos/mazos burtus
# is_palindrome("Alus ari ira      sula") -> True

def is_palindrome(text):
    text_reversed = text[::-1]
    text_reversed = text_reversed.split()#dividing in words - list
    text_reversed = " ". join(text_reversed)
    text = text.split()
    text = " ". join(text)
    print("upper", text.upper(), "->", text_reversed.upper())
    print("middle check", text == text_reversed)
    if text == text_reversed:
        result = True
    else:
        result = False
    return (text, "is palindrome? -> ", result)

print(is_palindrome("Alus ari ira      sula"))
print(is_palindrome("oho oho mmm oho oho"))


def is_palindrome2(text):
    my_text = text.upper().replace(" ","")
    return my_text == my_text[::-1]

print(is_palindrome2("Alus ari ira      sula"))
print(is_palindrome2("oho oho mmm oho oho"))