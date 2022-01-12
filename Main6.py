client_no = int(input('Please enter the clients number : '))
units_per_month = int(input('Please enter the units collected per month : '))

while True:
    status = input(' Please choose client status : X) old x. Y)new. [X/Y]?: ')
    if  status in ['X', 'Y']:
        break

while True:
    region = input(' Please choose region : X) region x. Y)region y. Z)region z. [X/Y/Z]?: ')
    if region in ['X', 'Y', 'Z']:
        break

if region == 'X':
    print('You have selected region x')
    price = 410

    total_cost = units_per_month * price


    if status == 'Y':
        discount = .15 * total_cost
        final_cost = total_cost - discount
        taxed_cost = final_cost + 200
        print('final cost is : ' + str(taxed_cost))
    else:
        taxed_cost = total_cost + 200
        print('final cost is : ' + str(taxed_cost))




elif region == 'Y':
    print('You have selected region Y')
    price = 450
    total_cost = units_per_month * price

    if status == 'X':
        discount = .1 * total_cost
        final_cost = total_cost - discount
        taxed_cost = final_cost * 1.16
        print('final cost is : ' + str(taxed_cost))
    else:
        taxed_cost = total_cost * 1.16
        print('final cost is : ' + str(taxed_cost))


elif region == 'Z':
    print('You have selected region Z')
    price = 490
    total_cost = units_per_month * price

    if status == 'X':
        discount = .1 * total_cost
        final_cost = total_cost - discount
        taxed_cost = final_cost * 1.16
        print('final cost is : ' + str(taxed_cost))
    else:
        taxed_cost = total_cost * 1.16

        print('final cost is : ' + str(taxed_cost))
