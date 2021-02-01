if __name__ == '__main__':
    product_price = input('Type the product price: ')
    product_price = float(product_price)

    value_added_tax = 24 / 100 * product_price
    print('The product price is: ' + str(product_price))

    monthly_instalment_price = (product_price + value_added_tax) / 10
    print('The monthly instalment is: ' + str(monthly_instalment_price))
