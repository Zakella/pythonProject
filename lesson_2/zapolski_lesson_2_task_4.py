price_list = [57.8, 46.51, 97, 100.11, 45.00, 11, 789.99, 89.90, 10, 15.55, 0.50]
price_list.sort()
for el in price_list:
    el = float(el)
    el = f"{el:.2f}"
    str_price = str(el).split(".")
    print(f"{str_price[0]} руб {int(str_price[-1]):02d} коп ")

new_price_list = price_list.copy()
new_price_list.sort(reverse=True)
print(new_price_list)
print(new_price_list[:5])
