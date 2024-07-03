def assign_buyer_to_seller(sellers, buyers_requests):
    seller = list(sellers.keys())[0]
    mapping = {}
    for (buyer, requested_item) in buyers_requests.items():
        for (seller, items_for_sale) in sellers.items():
            if requested_item in items_for_sale:
                mapping[buyer] = seller    
    return mapping

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

# output =  {
#   "buyer1" : "seller2",
#   "buyer2" :"seller1",
#   "buyer3" : "seller3",
#   "buyer4" : "seller2"
# }