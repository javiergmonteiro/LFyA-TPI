from nose.tools import istest, eq_
from floyd import floyd_algorithm

@istest
def matrix_INF_value_should_be_3():
    INF = 999
    test_matrix = [
        [0, 1, INF],
        [1, 0, 2],
        [INF, 2, 0]
    ]
    floyd_matrix = floyd_algorithm(test_matrix, 3)
    eq_(3, floyd_matrix[0][2])
    eq_(3, floyd_matrix[2][0])