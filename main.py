import logging
logging.basicConfig(level=logging.INFO)

def show_operation(operation,num1,num2):
    """
    Informs user about operations and arguments.
    Gets arguments from inputs at program start.
    All arguments should be integers.
    """
    if operation == 1:
        logging.info(f"Dodaję {num1} oraz {num2}.")
    elif operation == 2:
        logging.info(f"Odejmuję {num1} oraz {num2}.")
    elif operation == 3:
        logging.info(f"Mnożę {num1} oraz {num2}.")
    elif operation == 4:
        logging.info(f"Dzielę {num1} oraz {num2}.")
    else:
        logging.info('Nieznane działanie.')

if __name__ == "__main__":
    operation = int(input('Podaj działanie, posługując się odpowiednią liczbą: 1.Dodawanie, 2.Odejmowanie, 3.Mnożenie, '
                          '4.Dzielenie: '))
    num1 = int(input('Podaj pierwszą liczbę:'))
    num2 = int(input('Podaj drugą liczbę:'))

    show_operation(operation, num1, num2)

    if operation == 1:
        print('Wynik to:', num1+num2)
    elif operation == 2:
        print('Wynik to:', num1-num2)
    elif operation == 3:
        print('Wynik to:', num1*num2)
    elif operation == 4:
        print('Wynik to:', num1/num2)