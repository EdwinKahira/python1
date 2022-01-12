customers = 20

for customer in range(customers):
    while True:
        product_type = input(' Please choose a product : X) product x. Y)product y. [X/Y]?: ')
        if product_type in ['X', 'Y']:
            break

    units_sold = int(input('Please enter no of units sold : '))
    customer_nature = input(' Please choose your nature of customer : X) New x. Y)regular. [X/Y]?: ')

    if product_type == 'X':
        price = 600
        initial_purchase_value = price * units_sold
        print('Purchase value before discount :' + str(initial_purchase_value))

        if customer_nature == 'X' and initial_purchase_value >= 10000:
            discount = .1 * initial_purchase_value
            final_price = initial_purchase_value - discount
            print('discount is :' + str(discount))
            print('Purchase value after discount :' + str(final_price))

        elif customer_nature == 'Y' and initial_purchase_value >= 7500:
            discount = .15 * initial_purchase_value
            final_price = initial_purchase_value - discount
            print('discount is :' + str(discount))
            print('Purchase value after discount :' + str(final_price))

    if product_type == 'Y':
        price = 700
        initial_purchase_value = price * units_sold
        print('Purchase value before discount :' + str(initial_purchase_value))

        if customer_nature == 'Y' and initial_purchase_value >= 7500:
            discount = .15 * initial_purchase_value
            final_price = initial_purchase_value - discount
            print('discount is :' + str(discount))
            print('Purchase value after discount :' + str(final_price))
