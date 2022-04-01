def even_num(odd_numbers):
    k = 0
    summ = 0
    lg_number = len(str(odd_numbers))
    while k <lg_number:
        # val = str(odd_numbers)[k]
        val = odd_numbers % 10
        odd_numbers = odd_numbers // 10
        print(val)
        #  val  = odd_numbers // 10
        summ = summ + int(val)
        k = k + 1
    return summ

sum = even_num(123456)
print(sum)
