from sympy import *
from gauss_newton_nlr import gauss_newton_method


class regressionModel(object):
    def __init__(self, order):
        self.symbol_list = []
        self.init_coeff = []
        self.order = order


    def initialize_symbols(self):
        self.symbol_list = []
        for i in range(self.order):
            self.symbol_list.append(symbols('m{}'.format(i), real=True))
            #self.init_coeff.append(1.0)
        self.init_coeff = [15, 0.4, 10, 1]

    def initialize_coefficient(self):
        self.init_coeff = []
        for i in range(self.order):
            self.init_coeff.append(1.0)

    def get_sin_expression(self, x):
        self.initialize_symbols()
        sin_expr = self.symbol_list[0] * sin(self.symbol_list[1] * x + self.symbol_list[2]) + self.symbol_list[3]
        return sin_expr

    def get_exponential_expression(self, x):
        self.initialize_symbols()
        exponential_expr = self.symbol_list[0] * (1.0 - exp(-self.symbol_list[1] * x))
        return exponential_expr


def main():
    """x = symbols('x', real=True)
    model_obj = regressionModel(2)
    model = model_obj.get_exponential_expression(x)
    iteration_cnt = 20
    init_cnt = 0
    coefficient = gauss_newton_method(model_obj.init_coeff, init_cnt, iteration_cnt ,model,
                                      model_obj.symbol_list, x, model_obj.order)
    print 'coefficient:', coefficient"""

    x = symbols('x', real=True)
    model_obj = regressionModel(4)
    model = model_obj.get_sin_expression(x)
    iteration_cnt = 100
    init_cnt = 0
    coefficient = gauss_newton_method(model_obj.init_coeff, init_cnt, iteration_cnt, model,
                                      model_obj.symbol_list, x, model_obj.order)
    print 'coefficient:', coefficient


if __name__ == '__main__':
    main()