# 1. Simbolu biežums
# 1a. Uzrakstīt funkciju: get_char_count(text), kas saņem string un izvada vārdnīcu ar atsevišķu burtu lietojumu skaitu.
# get_char_count("hubba bubba") -> {'h': 1, 'u': 2, 'b': 5, 'a': 2, ' ': 1} # vārdnīcas secībai nav nozīme, un visam alfabetam nav jābut
# 1b. Uzrakstīt funkciju: get_digit_dict(num), kas saņem veselu skaitli kā parametru(var būt ļoti liels
# funkcija  izvada ciparu izmantojumu skaitlī vārdnīcas formā
# Ievada 599637003 -> {'0':2, '1':0,....'7'':1,'8':0,'9':2} # rādam visiem cipariem izmantojamību
# Ieverojam ka cipariskās atslēgas ir stringi
# PS 1a un 1b var atrisināt ar vienu un to pašu funkciju 1b vajadzībām nedaudz pielāgojot 1a kodu.
#  Var būt arī risinājums ar Counter but tas galīgi nav obligāti, lai gan ir ļoti eleganti :)

def get_char_count(text):
    text_str = sorted(str(text))
    char_list = []
    for n in text_str:
        if n not in char_list:
            char_list.append(n)

    char_dict = {i: text_str.count(i) for i in char_list}
    return char_dict

print(get_char_count("hubba bubba"))

def get_digit_dict(num):
    text_str = (str(num))
    char_dict = {str(i): text_str.count(str(i)) for i in range(10)}
    return char_dict

print(get_digit_dict(127777723334444555556666667788888888999999999))