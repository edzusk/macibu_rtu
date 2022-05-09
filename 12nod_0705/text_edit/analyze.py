# 1a -> uzrakstam funkciju file_line_len(fpath), kas atgriež rindiņu skaitu failā
# pārbaudam file_line_len("veidenbaums.txt") -> vajadzētu būt 971
# iespējams jums veidenbaums.txt nebūs tajā pašā mapē, tad lietojam relatīvo ceļu uz failu
import re
import string
from collections import Counter


def file_line_len(fpath):
    with open(fpath, encoding='utf-8') as f:
        return len(f.readlines())


#
# 1b -> uzrakstam funkciju get_poem_lines(fpath), kas atgriež list ar tikai tām rindiņām kurās ir dzeja.
# Tātad mums nederēs rindiņas bez teksta un nederēs dzejoļu virksraksti.
# PS vēlams izmantot encoding = "utf-8"a

def get_poem_lines(fpath):
    with open(fpath, encoding='utf-8') as f:
        poem_lines = []
        for line in f:
            if len(line.rstrip('\n')) > 0 and line.rstrip('\n')[-3:] != '***':
                poem_lines.append(line)
    return ''.join(poem_lines)


#
# 1c -> uzrakstam funkciju save_lines(destpath, lines)
# Šī funkcija noglabās destpath faila ceļā(tātad fails vai fails ar ceļu), visas lines

def save_lines(destpath, lines):
    with open(destpath, mode='w', encoding='utf-8') as f:
        f.writelines(lines)


# 1d -> izsaucam get_poem_lines uz veidenbaums.txt un tad rezultātu saglabājam veidenbaums_poems.txt (turpat kur ir jau veidenbaums) izmantojot save_lines funkciju


# 1e -> uzrakstam funkciju clean_punkts(srcpath,destpath)
# funkcija atvērs srcpath failu, attīrīs to no https://docs.python.org/3/library/string.html#string.punctuation
# un saglabās destpath
# izsaucam uz veidenbaums_poems.txt un destpath būs veidenbaums_no_punkts.txt

def clean_punkts(srcpath, destpath):
    with open(srcpath, encoding='utf-8') as inf, open(destpath, mode='w', encoding='utf-8') as outf:
        for line in inf:
            outf.write(line.translate(str.maketrans('', '', string.punctuation)))


# Droši vien nepietiks laika bet pamēģinam pa brīvdienām
# 1f -> uzrakstam funkciju get_word_usage(srcpath, destpath)
# funkcija atver failu un atrod biežāk lietotos vārdus
# ieteikums izmantot Counter moduli !
# uzskatīsim, ka vārdi tiek atdalīti vai nu ar whitespace vai newline (vecais labais split noderēs)
#
# populārāku vārdu sarakstu ar lietojuma biežumu saglabāam destpath
#
# Varam tagad pārbaudīt rezultātus gan uz veidenbaums_no_punkts.txt, gan uz veidenbaums_poems.txt


def get_word_usage(srcpath, destpath):
    with open(srcpath, encoding='utf-8') as inf, open(destpath, mode='w', encoding='utf-8') as outf:
        word_count = Counter(inf.read().lower().translate(str.maketrans('', '', string.punctuation)).split())
        for word, count in word_count.most_common():
            outf.write(f'{word} : {count} \n')
