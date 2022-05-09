
word_to_guess = list(input('ievadiet tekstu: ').lower)

hidden_word = []
for i in word_to_guess:
    if i == ' ':
        hidden_word.append(' ')
    else:
        hidden_word.append('*')

print(''.join(hidden_word))

guess_limit = 9
while guess_limit > 0:
    guess = input("ievadiet 1 burtu: ").lower
    if guess in word_to_guess:
        c = 0
        for i in word_to_guess:
            if i == guess:
                hidden_word[c] = i
                c += 1
            else:
                c += 1
        print(''.join(hidden_word))
    else:
        print(f'táda burta nav atlikuši {guess_limit} minējumi')
        guess_limit -= 1
    if hidden_word == word_to_guess:
        print('apsveicu, uzminēts,')
        break