from lib.depop import *

def test_assign_buyer_to_seller():
    sellers = {"seller2": ["shorts"]}
    buyers_requests = {"buyer1": "shorts"}
    bts = assign_buyer_to_seller(sellers, buyers_requests)
    assert bts == {"buyer1" : "seller2"}
    

def test_assign_multiple_buyers_to_single_seller():
    sellers = {"seller2": ["shorts"]}
    buyers_requests = {"buyer1": "shorts",
                       "buyer2": "shorts"}
    bts = assign_buyer_to_seller(sellers, buyers_requests)
    assert bts == {"buyer1" : "seller2",
                   "buyer2": "seller2"}
    

def test_assign_multiple_buyers_to_multiple_sellers_with_one_product():
    sellers = {"seller2": ["shorts"],
               "seller3": ["skirt"]}
    buyers_requests = {"buyer1": "shorts",
                       "buyer2": "skirt"}
    bts = assign_buyer_to_seller(sellers, buyers_requests)
    assert bts == {"buyer1" : "seller2",
                   "buyer2": "seller3"}
    

def test_assign_multiple_buyers_to_multiple_sellers_with_multiple_products():
    sellers = {"seller2": ["shorts", "trousers"],
               "seller3": ["skirt", "shirt"]}
    buyers_requests = {"buyer1": "trousers",
                       "buyer2": "shirt"}
    bts = assign_buyer_to_seller(sellers, buyers_requests)
    assert bts == {"buyer1" : "seller2",
                   "buyer2": "seller3"}
    

def test_example():
    sellers = {
    "seller1" : ["jeans", "t-shirt"],
    "seller2" : ["skirt", "dress"],
    "seller3" : ["coat"]
    }

    buyers_requests = {
    "buyer1" :"skirt",
    "buyer2" : "jeans",
    "buyer3" : "coat",
    "buyer4" : "skirt"
    }

    bts = assign_buyer_to_seller(sellers, buyers_requests)
    assert bts == {
        "buyer1" : "seller2",
        "buyer2" :"seller1",
        "buyer3" : "seller3",
        "buyer4" : "seller2"
        }