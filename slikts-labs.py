

def slikts_labs(text):
    nav_word = text.index('nav')
    slikts_word = text.index('slikts')
    if nav_word >= 0 and slikts_word >= 0 and nav_word < slikts_word:
        slikts_labs = f'{text[:nav_word]} ir labs'
        print(slikts_labs)
    else:
        print(text)

user_text = input('ievadiet textu: ')

slikts_labs(user_text)