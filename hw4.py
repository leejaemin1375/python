def rep_char(c, n) :
    print(c*n)
    
def draw_line_string(name) :
    msg1 = ('Hello ' + name + ',')
    msg2 = ('Welcome to Seoul.')
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-', nstr)
    print(f'{msg1:^s}')
    print(f'{msg2:^s}')
    rep_char('-', nstr )
    
draw_line_string(input('Input his/her name : '))
