# 6. nod. 2. uzd. "Kubu tabula"


user_start = int(input('enter first number: '))
user_end = int(input('enter last number: '))
cube_list = [n**3 for n in range(user_start, user_end +1)]
print(f'{cube_list=}')

# # OPTION 2
# def cube_numbers():
#     start_number = int(input('Enter starting number: '))
#     finish_number = int(input('Enter finish number: '))
#     cube_numbers = []
#     for i in range(start_number, finish_number +1):
#         cube_number = i**3
#         print(f'cube of {i} is {cube_number}')
#         cube_numbers.append(cube_number)
#     print(f"all cube's are {cube_numbers}")

# cube_numbers()


# # OPTION 3  without list
# def cube_numbers():
#     start_number = int(input('Enter starting number: '))
#     finish_number = int(input('Enter finish number: '))
#     cube_numbers = ''
#     for i in range(start_number, finish_number +1):
#         cube_number = i**3
#         print(f'cube of {i} is {cube_number}')
#         cube_numbers += str(cube_number)+","
#     print(f"all cube's are {cube_numbers}")

# cube_numbers()