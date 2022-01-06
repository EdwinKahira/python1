payroll_no = int(input('Please enter the payroll number : '))
hours_worked = int(input('Please enter the hours worked : '))
distance_travelled = int(input('Please enter the distance travelled in kilometers: '))
# Determine the type of grade

while True:
    grade = input(' Please choose workers Grade : X) Grade x. Y)Grade y. [X/Y]?: ')
    if grade in ['X', 'Y']:
        break
if grade == 'X':
    rate_per_hour = 1100
    mileage_rate = 50
    basic_pay = rate_per_hour * hours_worked
    mileage_pay = mileage_rate * distance_travelled
    house_allowance = 15000
    gross_pay = basic_pay + house_allowance + mileage_pay

    if gross_pay > 33000:
        # tax
        net_pay = gross_pay * .90
        tax = gross_pay * 0.1

        print('Employee payroll no : ' + str(payroll_no) + ' received : ' + str(net_pay) + ' net pay,  ' +
              str(gross_pay) + ' gross pay, and ' + str(tax) + ' was taxed')
    else:
        print('Employee payroll no : ' + str(payroll_no) + ' received : ' + str(gross_pay) + ' gross pay')


elif grade == 'Y':
    rate_per_hour = 1300
    mileage_rate = 90
    basic_pay = rate_per_hour * hours_worked
    mileage_pay = distance_travelled * mileage_rate

    if mileage_pay > 50000:
        mileage_pay = 50000
    else:
        mileage_pay = distance_travelled * mileage_rate

    gross_pay = basic_pay + mileage_pay

    if gross_pay > 33000:
        net_pay = gross_pay * .90
        tax = gross_pay * 0.1

        print('Employee payroll no : ' + str(payroll_no) + ' received : ' + str(net_pay) + ' net pay,  ' +
              str(gross_pay) + ' gross pay, and ' + str(tax) + ' was taxed')
    else:
        print('Employee payroll no : ' + str(payroll_no) + ' received : ' + str(gross_pay) + ' gross pay')