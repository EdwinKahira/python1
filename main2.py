salesperson_name = input('Write Salespersons name?: ')
name = input('Write your name?: ')
units = int(input('Enter number of units purchased: '))

while True:
    product = input(' Please choose a product : X) Product x. Y)product y. Z) product z. [X/Y/Z]?: ')
    if product in ['X', 'Y', 'Z']:
        break

if product == 'X':
    print('You have selected product x')
    price = 80


    def discount(total_amount):
        if total_amount > 10000:
            total_amount *= .85
        return print('Total is ksh ' + str(total_amount) + ' for ' + name + ' served by ' + salesperson_name)


    total_amount = price * units
    discount(total_amount)


elif product == 'Y':
    print('You have selected product y')
    price = 95
    total_amount = price * units
    taxed_amount = str(total_amount * 1.16)
    print('Total is ksh ' + taxed_amount + ' for ' + name + '  served by ' + salesperson_name)

elif product == 'Z':
    print('You have selected product z')
    price = 135
    total_amount = price * units
    print('Total is ksh ' + str(total_amount) + ' for ' + name + ' served by ' + salesperson_name)
