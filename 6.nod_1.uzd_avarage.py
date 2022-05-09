# 6. nod. 1.uzd. Avarage generator
def avarage():
    num_list = []
    while True:
        user_num = input('enter number or "q" to quit: ')

        if user_num == 'q':
            print('we are done ;)')
            break
        try:
            fl_num = round(float(user_num), 2)
            num_list.append(fl_num)
            avar_num = round(sum(num_list) / len(num_list))
            print(f'{avar_num=}')
            print(f'all entered numbers are {num_list} ')
            if len(num_list) > 3:
                top3 = sorted(num_list[:3])
                bottom3 = sorted(num_list[-3:])
                print(f'{top3=}')
                print(f'{bottom3=}')

        except ValueError:
            print('its not a number or "q"')
            pass


avarage()