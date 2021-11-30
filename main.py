from functions import *

if __name__ == "__main__":
    operation = (input('Podaj działanie, posługując się odpowiednią liczbą: 1.Dodawanie, 2.Odejmowanie, 3.Mnożenie, '
                          '4.Dzielenie: '))

    check_input_type(operation)
    check_operation_choice(operation)

    num1 = int(input('Podaj pierwszą liczbę:'))
    check_input_type(num1)

    num2 = int(input('Podaj drugą liczbę:'))
    check_input_type(num2)

    show_operation(operation, num1, num2)

    print_score(operation, num1, num2)
