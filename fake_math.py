
def divide(first, second):
    try:
        i = first/second
    except ZeroDivisionError:
        i = "Ошибка"
    else:
        i = first / second
    return  i



# result1 = divide(69, 3)
# result2 = divide(3, 0)
# # result3 = divide2(49, 7)
# # result4 = divide2(15, 0)
# print(result1)
# print(result2)
# # print(result3)
# # print(result4)