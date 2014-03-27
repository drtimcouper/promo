from nose.tools import *

import prog
import data




def test_no_products_with_promotions():
    products = ['pepsi']
    promos = {'coke': [data.two_for_one]}
    res = prog.calc_promos(products, promos)
    assert_equal(res, [])
