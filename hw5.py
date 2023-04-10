def read_single_digit(num):
    if num == 0:
        return '영'
    elif num == 1:
        return '일'
    elif num == 2:
        return '이'
    elif num == 3:
        return '삼'
    elif num == 4:
        return '사'
    elif num == 5:
        return '오'
    elif num == 6:
        return '육'
    elif num == 7:
        return '칠'
    elif num == 8:
        return '팔'
    elif num == 9:
        return '구'

def read_number(num):
    hundreds_digit = num // 100
    if hundreds_digit != 0:
        n1 = read_single_digit(hundreds_digit)
    
    tens_digit = (num // 10) % 10
    if tens_digit != 0:
        n2 = read_single_digit(tens_digit)
    
    ones_digit = num % 10
    if ones_digit != 0:
        n3 = read_single_digit(ones_digit)
        
    return n1 + n2 + n3


num = int(input('세 자리수 정수를 입력: '))
print(read_number(num))
