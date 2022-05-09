def median(sequence):
    sorted_sequence = sorted(sequence)
    sequence_Len = len(sequence)
    index = (sequence_Len - 1) // 2
    print(index)
 
    if sequence_Len % 2: # odd
        return sorted_sequence[index]
    else:
        if type(sequence) is str:
            return sorted_sequence[index] + sorted_sequence[index + 1]
        else:
            return (sorted_sequence[index] + sorted_sequence[index + 1]) / 2.0
 

 
def get_min_med_max(sequence):
    return min(sequence), median(sequence), max(sequence)
 
 
print(get_min_med_max([1, 5, 8, 4, 3]))  # 1345
# Output -> (1,4,8)
print(get_min_med_max([2, 2, 9, 9, 4, 3]))
# Output -> (2,3.5,9)
print(get_min_med_max("baaac"))
# Output -> ('a','a','c')
print(get_min_med_max("faaacb"))