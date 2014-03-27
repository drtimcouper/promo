from data import PROMOTIONS, PRODUCTS

promo_set = set(PROMOTIONS.iterkeys())

def calc_promo(products):
    # find all products which have promotions

    # intersection of skus and promotions .. set of all possible candidates

    promops = set(products) & promo_set

    retust = None

    return result


