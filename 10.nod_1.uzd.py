# Definējiet klasi Song
# Klases construktora vajag būt trīs papildu 3 parametriem(self un vēl 3!)
# title pēc noklusējuma tukša string
# author pēc noklusējuma tukšs string
# lyrics pēc noklusējuma tukšs tuple
# konstruktors saglabātu šos trīs parametrus
# un papildu izdrukātu uz ekrāna "New Song made" - (pamēģiniet arī izdrukāt šeit author un title!)
# Uzrakstiet metodi sing kas izdrukā dziesmu pa rindiņai uz ekrāna, vispirms izdrukājot autoru un title, ja tie ir.
# Uzrakstiet metodi yell kas izdrukā dziesmu ar lieliem burtiem pa rindiņai uz ekrāna, vispirms izdrukājot autoru un title, ja tie ir.
# Bonuss: uztaisiet lai sing un yell varam izsaukt vairākas reizes (ķēdejot)
# Bonuss: uztaisiet papildu parametru max_lines, kas izdrukā tikai noteiktu rindiņu skaitu gan sing gan yell. Labāk taisiet ar kādu default vērtību piem. -1 , pie kuras tad izdrukā visas rindas.
# Par ķēdēšano bija šeit: https://www.das.lv/platforma/mod/page/view.php?id=1794
# Izveidojiet vairākas dziesmas ar dziesmu tekstiem


class Song:
    def __init__(self, title='', author='', lyrics=()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f'New song made - "{self.title}" - "{self.author}"')

    def sing(self, end_line=-1):
        print(self.author, self.title)
        for line in self.lyrics[:end_line]:
            print(line)
        return self

    def yell(self, end_line=-1):
        self.upper_lyrics = (n.upper() for n in self.lyrics)
        print(self.author, self.title)
        print(*self.upper_lyrics, sep="\n")
        return self


ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])

ziemelmeita.sing(1)
ziemelmeita.yell()



stairway = Song('Stairway to heaven', 'Led Zeppelin',
                ["There's a lady who's sure all that glitters is gold", "And she's buying a stairway to heaven",
                 "When she gets there she knows, if the stores are all closed",
                 "With a word she can get what she came for", "Ooh, ooh, and she's buying a stairway to heaven"])
stairway.sing()
stairway.yell()



