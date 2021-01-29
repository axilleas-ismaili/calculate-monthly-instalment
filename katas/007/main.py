if __name__ == '__main__':
    product_price = input('Type product price: ')

    product_price = float(product_price)
    value_added_tax = 24/100 * product_price
    print(value_added_tax)
