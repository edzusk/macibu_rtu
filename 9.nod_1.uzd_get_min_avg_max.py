# Uzrakstiet funkciju get_min_avg_max(sequence), kas atgriež tuple ar trīs vērtībām attiecīgi mazāko, aritmētisko vidējo un lielāko vērtību no virknes.
# get_min_avg_max([0,10,1,9]) -> (0,5,10)
# ienākošā sequence var būt tuple vai list ar skaitliskām vērtībām.
# 1b tiem, kas pieredzējušāki
# Uzrakstiet funkciju get_min_med_max(sequence), kas atgriež tuple ar trīs vērtībām attiecīgi mazāko, medianu un lielāko vērtību no virknes.
# Median vērtība ir vērtiba, kas sakartotā virknē ir paša vidū. Ja virknes skaits ir pāra tad vidū ir divas vērtības.
# No vidus vērtībām tad ņem vidējo.
# get_min_med_max([1,5,8,4,3]) -> (1,4,8)
# get_min_med_max([2,2,9,9,4,3]) -> (2,3.5,9)
# get_min_med_max("baaac") -> ('a','a','c')
#  # ar string var būt interesanti rezultāti pie pāra skaita ņemot vidējo, tāpēc labak dot abus vidējos
# get_min_med_max("faaacb") -> ('a', 'ab', 'f')
# ienākošā sequence var būt tuple vai list ar vienāda tipa vērtībām, vai pat string.
import statistics
def get_min_avg_max(sequence):
    return min(sequence), statistics.mean(sequence), max(sequence)

print(get_min_avg_max([0,10,1,9]))

def get_min_med_max(sequence):
    # return min(sequence), statistics.median(sequence), max(sequence)
    sor_seq = sorted(sequence)
    if len(sequence) % 2:
        med = statistics.median(sequence)
    else:
        if type(sequence) is str:
            med = sor_seq[(len(sor_seq)-1) // 2] + sor_seq[(len(sor_seq)-1) // 2 + 1]
        else:
            med = statistics.median(sequence)
    return min(sequence), med, max(sequence)

print(get_min_med_max("baaac"))
print(get_min_med_max([1,5,8,4,3]))
print(get_min_med_max([2,2,9,9,4,3]))
print(get_min_med_max("faaacb"))
