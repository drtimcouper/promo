

PRODUCTS = {'coke': {"name":"coke", "price": 50},
            'crisps': {"name": "walkers", "price": 75},
            'sarni': {"name": "bacon", "price": 100},
            'boots': {"name": "boots", "price": 900}

            }



def two_for_one(*args):
    pass

def lowest_half_price(*args):
    pass

PROMOTIONS = {'coke': set([two_for_one,lowest_half_price]),
              'crisps': set([two_for_one]),
              'sarni': set([lowest_half_price])
            }
