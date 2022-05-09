# 2. Palindroms
# uzrakstiet funkciju is_palindrome(text)
# kas atgriež bool True vai False atkarībā vai vārds vai teikums ir lasāms vienādi no abām pusēm.
# PS no sākuma varat sākt ar viena vārda risinājumu, bet pilns risinājums ignorēs atstarpes(whitespace) un lielos/mazos burtus
# is_palindrome("Alus ari ira      sula") -> True

def is_palindrome(text):
    word_list = text.lower().split()
    flipped_stence = []
    for i in word_list[::-1]:
        flipped_stence.append(i[::-1])
    if word_list == flipped_stence:
        return True
    else:
        return False


print(is_palindrome("Alus ari ira      sula"))