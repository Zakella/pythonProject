def checkInt(s):
    isInt = True
    try:
        # converting to integer
        int(s)
    except ValueError:
        isInt = False
    if isInt:
        # print('Input value is an integer')
        return True
    else:
        # print('Not an integer')
        return False


def double_quote(word):
    return '"%s"' % word


num_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in range(len(num_list)):
    its_int = False
    for k in num_list[i]:
        if checkInt(k):
            its_int = True
    if its_int:
        if num_list[i].find("+") != -1:
            num_list[i] = f"+{int(num_list[i][-1]):02d}"
        elif num_list[i].find("5") != -1:
            num_list[i] = f"{int(num_list[i][-1]):02d}"
        num_list[i] = double_quote(num_list[i])

new_msg = ' '.join(num_list)
print(new_msg)
