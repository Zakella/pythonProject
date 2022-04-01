# def checkInt(str):
#     if str[0] in ('-', '+'):
#         return str[1:].isdigit()
#     return str.isdigit()

def checkInt(s):
    isInt = True
    try:
        # converting to integer
        int(s)
    except ValueError:
        isInt = False
    if isInt:
        print('Input value is an integer')
    else:
        print('Not an integer')


# def check_if_str_in_numbers(check_str):
#     s = '05'
#     isInt = True
#     try:
#         # converting to integer
#         int(s)
#     except ValueError:
#         isInt = False
#     if isInt:
#         print('Input value is an integer')
#     else:
#         print('Not an integer'
#
# check_if_str_in_numbers("05"):

#
#
num_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
only_numb = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




for i in range(len(num_list)):
    num_list[i] = f'"{num_list[i]}"'
    el_in_list = num_list[i]
    if not el_in_list.find("5") == -1:
        el_int = el_in_list[-2]
        ind = el_in_list.find('5')
        if not el_in_list.find("+") == -1:
            num_list[i] = f"+{int(el_int):02d}"
        else:
            num_list[i] = f"{int(el_int):02d}"
    num_list[i] = f'"{num_list[i]}"'
    print(num_list[i])
    print(type(num_list[i]))
    print(checkInt( num_list[i]))

print(num_list)

    # elif el_in_list.find("5") != -1:
# ind = el_in_list.find('5')
# num_list[i] = f"{int(el_in_list[ind]):02d}"
# num_list[i] = f'"{num_list[i]}"'
# if not check_if_str_in_numbers(num_list[i]):
#     num_list[i] = num_list[i] .replace("""""", '')

# print(num_list)
# print(el_in_list)
# print(num_list)
# new_msg = ''.join(num_list)
# print(new_msg)
# # print(el_in_list)
# if checkInt(el_in_list):
#     if not el_in_list.find("5") == -1:
#         el_int = el_in_list[-1]
#         if not el_in_list.find("+") == -1:
#            num_list[i] = f" +{int(el_int):02d}"
#         else:
#             num_list[i] = f" {int(el_int):02d}"


# new_msg = ','.join(num_list)
# print(new_msg)
