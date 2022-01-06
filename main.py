name = input('Write your name?:')

cost = 7

# select old or new tea picker

while True:
    picker_type = input('A)Old tea picker. B) New tea picker [A/B]:')
    if picker_type in ['A', 'B']:
        break

    if picker_type == 'A':
        print('You have selected Old tea picker')

    elif picker_type == 'B':
        print('You have selected on New tea picker')

if picker_type == 'A':
    allowance = 100
else:
    allowance = 50


def kilo_bonuses(kilos):
    bonus_list = []
    if kilos > 20:
        bonus_kilos = kilos - 20
        bonus = int(bonus_kilos * 4)
        wages = bonus + allowance + kilos * cost
        print('Total Bonus for' + name + ' is : ' + str(bonus))
        print('Total wages are : ' + str(wages))
        bonus_list.append('bonus for ' + name + ' is ' + str(bonus))

    else:
        wages = allowance + kilos * cost
        print('Total wages are : ' + str(wages) + ' with no bonus')

    return print(bonus_list)


kilos = int(input('Enter no of kilos: '))
kilo_bonuses(kilos)

