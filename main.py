if __name__ == '__main__':
    """
    Ένα κατάστημα προσφέρει 10 άτοκες μηνιαίες δόσεις στα προϊόντα του. 
    """
    print('Type product price: ')
    productPrice = input()
    print('The product price is ' + productPrice)

    floatProductPrice = float(productPrice)
    valueAddedTax = (24 / 100) * floatProductPrice
    print('The value added tax is ' + str(valueAddedTax))
