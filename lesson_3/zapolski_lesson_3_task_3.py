import random


def there_is_a_repeat(list):
    pass


def generate_joke(no_reapeats, first_joke=False):
    list = []
    list.append(random.choice(nouns))
    list.append(random.choice(adverbs))
    list.append(random.choice(adjectives))
    if not first_joke and no_reapeats:
        for it in list:
            for g_el in final_list:
                l_split = g_el.split()
                for str_l in l_split:
                    if not str_l.find(it) == -1:
                        print("repeat")
                        # generate_joke(no_reapeats, True)


            #
            #     #generate_joke(no_reapeats, True)

    #
    # random.choice(nouns)
    # random.choice(adverbs)
    # random.choice(adjectives)
    # print(type(random.sample(nouns, 1)))
    # A = "" +random.sample(nouns, 1) + " " + random.sample(adverbs, 1) + " " + random.sample(adjectives,1)
    # return A
    return " ".join(list)

    # a = list(set(list) & set(final_list))
    # print(a)

    # return list


def get_jokes(n, no_reapeats=False):
    global final_list
    final_list = []
    for i in range(n):
        final_list.append(generate_joke(no_reapeats))

    return final_list

    # for i in range(len(final_list)):
    #     # print(final_list[i])
    #     print(final_list[i + 1])


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(2, True))
#
# list = []
# # list.append(random.choice(nouns))
# # list.append(random.choice(adverbs))
# # list.append(random.choice(adjectives))
# list.append(random.sample(nouns, 1))
# list.append(random.sample(adverbs, 1))
# list.append(random.sample(adjectives, 1))
#
# list.append(random.sample(nouns, 1))
# list.append(random.sample(adverbs, 1))
# list.append(random.sample(adjectives, 1))

# list1 = []
# list1.append(random.sample(nouns, 1))
# list1.append(random.sample(adverbs, 1))
# list1.append(random.sample(adjectives, 1))
# print(list1)
#
# list2 = []
# list2.append(random.sample(nouns, 1))
# list2.append(random.sample(adverbs, 1))
# list2.append(random.sample(adjectives, 1))
# print(list2)

# numbersList = [1, 2, 3]
# str_list = ['one', 'two']
# numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')
#
# # Notice, the size of numbersList and numbers_tuple is different
# result = zip(numbersList, numbers_tuple)
# print(*result)
