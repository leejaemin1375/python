shopping_bag = {}

while True:
    item = input('상품명? ')
    if item == "":
        break
    amount = int(input('수량은? '))
    shopping_bag[item] = amount
    print(f'장바구니에 {item} {amount}개가 담겼습니다.\n')

print(f'장바구니 보기: {shopping_bag} \n')

print('[검색]')
search_item = input('장바구니에서 확인하고자 하는 상품은? ')
print(f'{search_item}은(는) {shopping_bag[search_item]}개 담겨 있습니다.')
