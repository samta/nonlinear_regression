from linear_algebra import *
#from config import *
from data import *
"""
Y = a0*(1-e^(-a1*X))
Calculate a0, a1 using Gauss Newton
"""

def get_jacobian_matrix(coeff, expr, symbol_list, variable):
    """
    input: list of coeffcient
    :return: A = [partial differentiation of Xin wrt a0 and a1] mxn
    """
    print coeff
    print symbol_list
    jacobian_matrix = []
    d = {}
    for c, s in zip(coeff, symbol_list):
        d[s] = c
    for size in range(data_size):
        row = []
        d[variable] = Xin[size]
        for i in range(len(coeff)):
            part_diff = (expr.diff(symbol_list[i])).subs(d)
            row.append(part_diff)
        jacobian_matrix.append(row)
    return jacobian_matrix


def get_residue_matrix(coeff, expr, symbol_list, variable):
    """
    :return: [Yin-f(Xin)]mxn
    """
    residue_matrix = []
    d = {}
    for c, s in zip(coeff, symbol_list):
        d[s] = c
    for xin,yin in zip(Xin, Yin):
        d[variable] = xin
        residue_matrix.append([yin-expr.subs(d)])

    return residue_matrix


def get_coefficient_matrix(A, B, order):
    """
    For input A and B matrix, compute Z which is coefficient of matrix
    A^T*A*Z = A^T*B
    :return: [a0, a1]
    """
    AT = getTranspose(A, len(A), order)
    return getMultiplication(getMatrixInverse(getMultiplication(AT, A)), getMultiplication(AT, B))


def gauss_newton_method(init_coeff, init_cnt, iteration_cnt, expr, symbol_list, variable, order):
    print 'COUNT:', init_cnt
    A = get_jacobian_matrix(init_coeff, expr, symbol_list, variable)
    B = get_residue_matrix(init_coeff, expr, symbol_list, variable)
    #print 'A:', A
    #print 'B:', B
    coefficient = get_coefficient_matrix(A, B, order)
    coeff_size = len(init_coeff)
    print 'coefficient>>>>',coefficient, coeff_size, init_coeff
    #print '>>>>>>>', coefficient, init_coeff, coefficient[0][0], coefficient[1][0], coeff_size
    curr_coeff = [round(coefficient[i][0]+init_coeff[i], 2) for i in range(coeff_size)]
    print '>>>>',init_coeff,  curr_coeff
    #print 'Coeffieicnt:', init_coeff, curr_coeff
    #print 'cnt', init_cnt
    termination = True
    for i in range(coeff_size):
        print 'diff', abs(init_coeff[i]-curr_coeff[i])
        if abs(init_coeff[i]-curr_coeff[i]) > 0.1:
        #if init_coeff[i] != curr_coeff[i]:
            termination = False
    print termination
    if termination is True or  init_cnt == iteration_cnt:
        print 'returning', curr_coeff
        return curr_coeff
    init_cnt = init_cnt + 1
    #return
    return gauss_newton_method(curr_coeff, init_cnt, iteration_cnt, expr, symbol_list, variable, order)
    #return curr_coeff


#coeffieicnt = gauss_newton_method(init_coeff, iteration_cnt, init_cnt, expr, symbol_list)
#print coeffieicnt
