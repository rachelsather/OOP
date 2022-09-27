class PayrollDeduction:

    def __init__(self,description,date,charge_amt,employee_id):
        self.__description = description
        self.__date = date
        self.__charge_amt = charge_amt
        self.__employee_id = employee_id


    def get_description(self):
        return self.__description
    def get_date(self):
        return self.__date
    def get_charge_amt(self):
        return self.__charge_amt
    def get_employee_id(self):
        return self.__employee_id


    def deduction(self, charge_amt):
        self.__balance -= abs(charge_amt)

    def get_net_pay(self):
        return self.__balance

    