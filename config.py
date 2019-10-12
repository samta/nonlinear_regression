from sympy import *
iteration_cnt = 20
init_cnt = 0
order = 2
symbol_list = []
init_coeff = []
x = symbols('x', real=True)
for i in range(order):
    symbol_list.append(symbols('m{}'.format(i), real=True))
    init_coeff.append(1.0)

expr = symbol_list[0]*(1.0-exp(-symbol_list[1]*x))
exponential_expr = symbol_list[0]*(1.0-exp(-symbol_list[1]*x))

order = 4
for i in range(order):
    symbol_list.append(symbols('m{}'.format(i), real=True))
    init_coeff.append(1.0)

sin_expr = symbol_list[0]*sin(symbol_list[1]*x+symbol_list[2])+symbol_list[3]
