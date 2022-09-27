import EmployeeClass as E
import PayrollDeductionClass as P

def main():
    Jimmy = E.Employee('Jimmy Smith', 58475, 'Information Systems', 'Developer', 6800.00)
    
    balance = Jimmy.get_monthly_salary()

    Deduction1 = P.PayrollDeduction('food court', '8/14/2022', 22.50, 39119)
    Deduction2 = P.PayrollDeduction('gift contribution', '8/12/2022', 25.00, 58475)
    Deduction3 = P.PayrollDeduction('food court', '8/17/2022', 15.25, 21547)
    Deduction4 = P.PayrollDeduction('vending machine', '8/22/2022', 3.00, 58475)
    Deduction5 = P.PayrollDeduction('vending machine', '8/5/2022', 2.75, 58475)

    if Deduction1.get_employee_id() == Jimmy.get_id_number():
        balance -= Deduction1.get_charge_amt()
    if Deduction2.get_employee_id() == Jimmy.get_id_number():
        balance.deduction(Deduction2.get_charge_amt)
    if Deduction3.get_employee_id() == Jimmy.get_id_number():
        balance.deduction(Deduction3.get_charge_amt)
    if Deduction4.get_employee_id() == Jimmy.get_id_number():
        balance.deduction(Deduction4.get_charge_amt)
    if Deduction5.get_employee_id() == Jimmy.get_id_number():
        balance.deduction(Deduction5.get_charge_amt)

    print('*** Employee Pay ***')
    print('Name: ', Jimmy.get_name())
    print('ID Number: ', Jimmy.get_id_number())
    print('Department: ', Jimmy.get_department())
    print('Gross Pay: $', format(Jimmy.get_monthly_salary(), ',.2f'), sep='')
    print('Net Pay: $', format(balance, ',.2f'), sep='')
    #print(balance.get_net_pay(), ',.2f'), sep='')

main()

