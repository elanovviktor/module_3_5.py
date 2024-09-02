def get_multiplied_digits(namber):# создали функцию с параметром
    str_number = str (namber)# переменная в строковом и числом в ней
    first = int(str_number[0])  # создали переменную first и завели в нее первую цифру из строки number
    if len(str_number)>1:# отделяям первую цифру в числе

        return first * get_multiplied_digits(int(str_number[1:]))# делаем согласно 4 пукту дз
    elif first != 0:
        return first

    else:
        return 1

result = get_multiplied_digits(40203)
print(result)

