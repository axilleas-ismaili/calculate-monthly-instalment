if __name__ == '__main__':
    """
    emfanise("plhktrologise  timi proiontos")
    timi proiontos = diavase tin timi pou tha plhktrologithi
    emfanise ('h timi proiontos einai' + timi proiontos) 
    """
    print('Type product price in euros: ')
    product_price = input()
    print('The product price is ' + product_price + ' euros.')

    """
    metetrepse se dekadiko thn timi tou proiontos 
    Φ.Π.Α = (epitokio/100)*timiproiontos
    emfanise to Φ.Π.Α 
    """
    float_product_price = float(product_price)
    value_added_tax = (24 / 100) * float_product_price
    print('The value added tax is ' + str(value_added_tax) + ' euros.')

    """
    timi_minieas_dosi = (timi_prointos + value_added_tax) / sinolikes_doseis
    emfanise timi_minieas_dosis   
    """
    monthly_instalment_price = (float_product_price + value_added_tax) / 10
    print('The monthly instalment price is ' + str(monthly_instalment_price) + ' euros.')

    """
    sinoliki_aksia_proiontos = timi_minieas_dosi * 10
    emfanise sinoliki_aksia_proiontos
    """
    total_product_price = monthly_instalment_price * 10
    print('Total product price is ' + str(total_product_price) + ' euros.')
