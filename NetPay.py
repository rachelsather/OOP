import EmployeeClass as E
import PayrollDeductionClass as P

def main():
    Jimmy = E.Employee('Jimmy Smith', 58475, 'Information Systems', 'Developer', 6800.00)
    
    balance = Jimmy.get_monthly_salary()

    Deductions = (P.PayrollDeduction('food court', '8/14/2022', 22.50, 39119), 
        P.PayrollDeduction('gift contribution', '8/12/2022', 25.00, 58475), 
        P.PayrollDeduction('food court', '8/17/2022', 15.25, 21547), 
        P.PayrollDeduction('vending machine', '8/22/2022', 3.00, 58475),
        P.PayrollDeduction('vending machine', '8/5/2022', 2.75, 58475))

    for i in Deductions:
        if i.get_employee_id() == Jimmy.get_id_number():
            balance -= i.get_charge_amt()

    print('*** Employee Pay ***')
    print('Name: ', Jimmy.get_name())
    print('ID Number: ', Jimmy.get_id_number())
    print('Department: ', Jimmy.get_department())
    print('Gross Pay: $', format(Jimmy.get_monthly_salary(), ',.2f'), sep='')
    print('Net Pay: $', format(balance, ',.2f'), sep='')

main()

