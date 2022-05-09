# 7.nod 1.uzd
# Uzrakstiet funkciju add_mult, kurai nepieciešami trīs parametri/argumenti
# Atgriež rezultātu, kas ir 2 mazāko argumentu summa reizināta ar lielāko argumenta vērtību.
# PS Uzskatīsim, ka funkcijai vienmēr tiks padoti skaitliski parametri, varam tipus nepārbaudīt.
# Iespējami dažādi risinājumi, piemēram ar list struktūru varētu būt tīri eleganti.
# Piemērs add_mult(2,5,4) -> atgriezīs (2+4)*5 = 30

def add_mult(*nums):
    num_list = []
    for num in nums:
        num_list.append(num)

    arg_list = sorted(num_list)
    return (sum(arg_list[:-1])*arg_list[-1])



print(add_mult(5,1,1,1,77))
