# CTI-110

# P4HW2 - Salary

# Tory Horton

# 4-27-23


 
# how many employees the user wants to enter

employee_num = 0

# regular employee pay

employee_reg_pay = 0

# overtime pay

employee_overtime_pay = 0

employee_gross_pay = 0 # gross pay 

# start loop for salaries

employee_name = 'Done'

while True:

    print()

    employee_name != 'Done' 

    employee_name = input("Enter employee's name or Done to terminate: ") # for user to teminate type Done

    if employee_name == 'Done':
        break

    else:

        employee_num += 1

    hours_worked = float(input("How many hours did they work? ")) # asks # of hours worked

    pay_rate = float(input("What is their pay rate? ")) # asks employee's pay rat

    reg_pay = 0 # regular pay

    overtime = 0 # overtime

    overtime_pay = 0 # overtime pay

    gross_pay = 0 # gross pay

    if hours_worked >= 40: # executes if hours worked is more than 40

        overtime_pay_rate = 1.5

        overtime = hours_worked - 40 # used to find overtime amount

        reg_pay = (hours_worked - overtime) * pay_rate

        overtime_rate = overtime * overtime_pay_rate # used to find overtime rate

        overtime_pay = pay_rate * overtime_rate # used to find overtime pay

        gross_pay = overtime_pay + reg_pay

    else:

        reg_pay = (hours_worked * pay_rate)

        gross_pay = reg_pay # finds the gross pay
        

# ----------------------------------------
    employee_reg_pay += reg_pay

    employee_gross_pay += gross_pay

    employee_overtime_pay += overtime_pay

# ----------------------------------------
    print()

    print(f'{"Employee name:":<20}{employee_name:<10}') # displays employee's name

    print()

    print('Hours Worked    Pay Rate    Overtime    OverTime Pay    RegHour Pay    Gross Pay')

    print('-----------------------------------------------------------------------------------------')

    print()

    print(f'{hours_worked:.1f}{pay_rate:17.1f}{overtime:11.1f}{overtime_pay:14.2f}{reg_pay:16.2f}{gross_pay:15.2f}')

print(f'{"Total number of employees entered: "}{employee_num}') # displays number of employees
print(f'{"Total amount paid for overtime: ":}${employee_overtime_pay:.2f}') # displays overtime for employees
print(f'{"Total amount paid for regular hours: "}${employee_reg_pay:.2f}') # displays regular pay of employees
print(f'{"Total amount paid in gross: "}${employee_gross_pay:.2f}') # displays gross employee pay




    
