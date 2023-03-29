def get_fixed_price(prompt):
    rate =  (100-prompt)*(1/100)
    return rate

money = int(input('할인율은? ')) 
discount_price_A = int(input('A 상품의 할인된 가격은? '))
discount_price_B = int(input('B 상품의 할인된 가격은? '))
print('A 상품의 정가는', int(discount_price_A/get_fixed_price(money)), '원')
print('B 상품의 정가는', int(discount_price_B/get_fixed_price(money)), '원')
