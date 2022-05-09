# 1a -> uzrakstam funkciju file_line_len(fpath), kas atgriež rindiņu skaitu failā
# pārbaudam file_line_len("veidenbaums.txt") -> vajadzētu būt 971
# iespējams jums veidenbaums.txt nebūs tajā pašā mapē, tad lietojam relatīvo ceļu uz failu

from pathlib import Path
import text_edit.analyze

veiden_path = Path(__file__).parent.resolve() / 'textfiles' / 'veidenbaums.txt'
poem_veiden_path = Path(__file__).parent.resolve() / 'textfiles' / 'veidenbaums_poems.txt'
no_punkt_path = Path(__file__).parent.resolve() / 'textfiles' / 'veidenbaums_no_punkts.txt'
word_count_path = Path(__file__).parent.resolve() / 'textfiles' / 'word_count.txt'
# a
print(text_edit.analyze.file_line_len(veiden_path))

# b
print(text_edit.analyze.get_poem_lines(veiden_path))

# c, d

text_edit.analyze.save_lines(poem_veiden_path, text_edit.analyze.get_poem_lines(veiden_path))

# e
text_edit.analyze.clean_punkts(veiden_path, no_punkt_path)

# f
text_edit.analyze.get_word_usage(veiden_path, word_count_path)
