# uzrakstīt funkciju is_pangram, kas atgriež True, kad mytext parametrs satur visus burtus kas padoti a alfabetā.
# Savadāk atgriežam False.
# pangramma - teikums,vārdu virkne, kas satur visus alfabeta burtus - https://en.wikipedia.org/wiki/Pangram
# Atstarpes ignorējam,un uzskatam ka lielais burts ir tikpat derīgs kā mazais, t.i. šeit A un a -> a


import string
def is_pangram(text, a=string.ascii_lowercase):
    print(set(text.replace(' ', '').lower()))
    print(set(string.ascii_lowercase))
    return set(a) >= set(text.lower())

print(is_pangram("The five boxing wizards jump quickly"))

