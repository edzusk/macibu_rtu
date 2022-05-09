# 2. Vārdnīcu labotājs
# Uzrakstīt replace_dict_value(d, bad_val, good_val), kas atgriež vārdnīcu ar nomainītām vērtībām
# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtības bad_val kura jānomaina uz good_val
# replace_dict_value({'a':5,'b':6,'c':5}, 5, 10) -> {'a':10,'b':6,'c':10} , jo 5 bija vērtība, kas jānomaina.


def replace_dict_value(d, bad_val=5, good_val=10):
    good_dict = {key: (good_val if val == bad_val else val) for key, val in d.items()}

    # good_dict = {}
    # for key, value in d.items():
    #     if value == bad_val:
    #         good_dict[key] = good_val
    #     else:
    #         good_dict[key] = value
    return good_dict

print(replace_dict_value({'a':5,'b':6,'c':5, 'd':7, 'e':8, 'f':10}, 7, 0))
print(replace_dict_value({'a':5,'b':6,'c':5}, 5, 10))
print(replace_dict_value({'a':5,'b':6,'c':5}))
