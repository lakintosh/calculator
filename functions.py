import logging
logging.basicConfig(level=logging.INFO)

def check_operation_choice(user_input):
    '''
    Checks if operation number is correct.
    :param user_input:
    '''
    if int(user_input) < 1 or int(user_input) > 4:
        logging.info('Nieznane działanie.')
        exit()
    else: pass

def show_operation(operation, num1, num2):
    """
    Informs user about operations and arguments.
    Gets arguments from inputs at program start.
    All arguments should be integers.
    """
    if int(operation) == 1:
        logging.info(f"Dodaję {num1} oraz {num2}.")
    elif int(operation) == 2:
        logging.info(f"Odejmuję {num1} oraz {num2}.")
    elif int(operation) == 3:
        logging.info(f"Mnożę {num1} oraz {num2}.")
    elif int(operation) == 4:
        logging.info(f"Dzielę {num1} oraz {num2}.")

def check_input_type(user_input):
    """
    Checks if provided value is an integer.
    Takes users input as an argument.
    """
    if type(user_input):
        pass
    else:
        print('Podana wartość musi być liczbą!')
        exit()

def print_score(operation, num1, num2):
    '''
    Prints score depending on chosen operation
    arguments: operation, first number, second number
    '''
    if int(operation) == 1:
        print('Wynik to:', num1 + num2)
    elif int(operation) == 2:
        print('Wynik to:', num1 - num2)
    elif int(operation) == 3:
        print('Wynik to:', num1 * num2)
    elif int(operation) == 4:
        if num2 == 0:
            print('Nie dzielimy przez zero!')
        else:
            print('Wynik to:', num1 / num2)
