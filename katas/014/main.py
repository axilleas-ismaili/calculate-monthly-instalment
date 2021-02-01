if __name__ == '__main__':
    product_price = input('Type the product price: ')
    product_price = float(product_price)
    
    value_added_tax = 24 / 100 * product_price
    print(value_added_tax)

    monthly_instalment_price = (product_price + value_added_tax) / 10
    print(monthly_instalment_price)
