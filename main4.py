sale_persons = 50
price = 1200
t_x = 0
t_y = 0
t_z = 0
for sale_person in range(sale_persons):
    units = int(input('No of units sold: '))
    name = input('Sales persons name : ')
    while True:
        region = input(' Please choose a region : X) region x. Y)region y. Z) region z. [X/Y/Z]?: ')
        if region in ['X', 'Y', 'Z']:
            break
    if region == 'X':
        def commission_x(price):
            commission_earned = 0.15 * price
            total_commission = commission_earned * units
            print(name + ' has earned a commission of ' + str(total_commission))
            if total_commission > 14000:
                net_commission = total_commission * .90
                print(name + 's  commission has been reduced to ' + str(net_commission)+' net commission after tax')
                return net_commission

            if units > 300:
                bonus = (units - 300) * .10
                total_commission += bonus
                print(name + ' has earned a commission of ' + str(total_commission))
                if total_commission > 14000:
                    net_commission = total_commission * .90
                    print(name + 's  commission has been reduced to ' + str(net_commission)+' net commission after tax')
                    return net_commission

            return total_commission

        t_x += commission_x(price)


    elif region == 'Y':
        def commission_y(price):
            commission_earned = 0.18 * price
            total_commission = commission_earned * units
            print(name + ' has earned a commission of ' + str(total_commission))

            if total_commission > 14000:
                net_commission = total_commission * .90
                print(name + '  commission has been reduced to ' + str(net_commission)+' net commission after tax')
                return net_commission


            if units > 300:
                bonus = (units - 300) * 15
                total_commission += bonus
                print(name + ' has earned a commission of ' + str(total_commission))
                if total_commission > 14000:
                    net_commission = total_commission * .90
                    print(name + 's  commission has been reduced to ' + str(net_commission)+' net commission after tax')
                    return net_commission

            return total_commission

        t_y += commission_y(price)

    elif region == 'Z':
        def commission_z(price):
            commission_earned = 0.19 * price
            total_commission = commission_earned * units
            print(name + ' has earned an initial commission of ' + str(total_commission))
            if total_commission > 14000:
                net_commission = total_commission * .90
                print(name + '  commission has been reduced to ' + str(net_commission) + ' net commission after tax')
                return net_commission
            if units > 300:
                bonus = (units - 300) * 15
                total_commission += bonus
                print(name + ' has earned a commission of ' + str(total_commission))
                if total_commission > 14000:
                    net_commission = total_commission * .90
                    print(name + '  commission has been reduced to ' + str(net_commission)+' net commission after tax')
                    return net_commission

            return total_commission


        t_z += commission_z(price)


print('total commission for region x is : ' + str(t_x))
print('total commission for region y is : ' + str(t_y))
print('total commission for region z is : ' + str(t_z))
