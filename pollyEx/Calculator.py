# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'


class Calculator():

    def __init__(self, amount, interest, downpayment, term):
        self.amount = int(amount)
        self.interest = float(interest)
        self.downpayment = int(downpayment)
        self.term = int(term)

    def __repr__(self):
        return ('class Calculator:\namount={}\ninterest={}\ndownpayment={}\nterm={}'.format(self.amount,
                                                                                          self.interest,
                                                                                          self.downpayment,
                                                                                          self.term))

    def calculate(self):
        cost = self.amount - self.downpayment
        monthly_payments = (cost*self.interest/(100*12))/(1 - (1 + self.interest/(100*12))**(-self.term*12))
        total_payments = monthly_payments*self.term*12
        total_interest = round(total_payments, 2) - (self.amount - self.downpayment)


        return {'monthly_payments': round(monthly_payments, 2),
                'total_interest': round(total_interest, 2),
                'total_payments': round(total_payments, 2)}


    def mortgage(self):
        pass