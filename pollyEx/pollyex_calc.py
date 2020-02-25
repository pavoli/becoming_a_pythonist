# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'


from pollyEx.Calculator import Calculator


"""
Your program is going to get data from standard input in the following format:

```
amount: 100000
interest: 5.5%
downpayment: 20000
term: 30

```
NOTE:
a) the last line of input is a blank line.
b) The term is given in years.
c) The interest can be given a percentage or a digit.

Your program needs to process the input including handling some human errors
(upper/lower case, spacing etc) and output a JSON of the monthly payment
and total interest paid.

```
{
    "monthly payment": 454.23,
    "total interest": 83523.23
    "total payment" 163523.23
}
```
"""

data = {
    'amount': [
        'Please enter the amount you need, only number, like 100000 or 90000',
        'number',
        '',
    ],
    'interest': [
        'Please enter the interest, number or decimal, like 5 or 5.5',
        'decimal',
        '',
    ],
    'downpayment': [
        'Please enter the downpayment, only number, like 5000 or 10000',
        'number',
        '',
    ],
    'term': [
        'Please enter the term you need, only number, like 10 or 30',
        'number',
        '',
    ],
}


source_data = {}


def main():
    print('Welcome to our "Simple Mortgage Calculator"!')
    print('To count month payment I need to know following data: amount, interest, downpayment, term')
    print('How do you want to provide data?')
    while (True):
        choose = input('Please type (1) manually or (2) file?')
        try:
            choose = int(choose)
            if choose not in [1, 2]:
                print('You choose {}, but I understand only 1 or 2'.format(choose))
            else:
                break
        except:
            print('May be it was by mistake...You typed the letter')
            print('Please, type 1 or 2')
    print('You choose {}'.format(choose))

    mortgage_calc(choose)
    amount, interest, downpayment, term = source_data.values()
    calc = Calculator(amount=amount, interest=interest, downpayment=downpayment, term=term)


    return (calc.calculate())


def mortgage_calc(choose):
    if choose == 1:
        read_keyboard()
    elif choose == 2:
        read_file()


def read_keyboard():
    for key, value in data.items():
        # print(key, value[1])
        while True:
            inp = input(value[0])
            try:
                inp = int(inp)
                value[2] = inp
                source_data[key] = inp
                break
            except:
                try:
                    inp = float(inp)
                    source_data[key] = inp
                    break
                except:
                    print('Try again...please, type ONLY {}'.format(value[1]))
        print('{}={}'.format(key, inp))
    print_dict(source_data)


def print_dict(d):
    print('You enter:')
    for key, value in d.items():
        print('{}={}'.format(key, value))



def read_file():
    result = {}
    while True:
        file_name = input('Please, input correct FILE_NAME')
        try:
            with open(file_name, mode='r') as data:
                d = data.read().split('\n')
                for i in d:
                    if i.strip():
                        name, value = i.split(':')
                        name = name.lower().strip()
                        value = value.rstrip('%').strip()
                        source_data[name] = value
            break
        except Exception as e:
            print("Error= {}".format(e))

    print_dict(source_data)



if __name__ == '__main__':
    main()