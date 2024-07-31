class Pizza:
    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = price

    def display_pizza_details(self):
        print(f"Pizza: {self.name}")
        print(f"Ingredients: {self.ingredients}")
        print(f"Price: £{self.price}")

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        print(f"{ingredient} added to {self.name}")

    def remove_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)
            print(f"{ingredient} removed from {self.name}")
        else:
            print(f"{ingredient} not in {self.name}")


class PizzaRestaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu

    def display_menu(self):
        print(f"Menu at {self.name}:")
        for pizza in self.menu:
            pizza.display_pizza_details()
            print()

    def order_pizza(self, pizza_name):
        for pizza in self.menu:
            if pizza.name == pizza_name:
                print(f"Order confirmed for {pizza.name}!") 
                pizza.display_pizza_details()
                return pizza
        print(f"We're out of {pizza_name}")
        return None

margherita = Pizza("Margherita", ["Tomato sauce", "Mozzarella", "Basil"], 8.00)
hawaiian = Pizza("Hawaiian", ["Tomato sauce", "Mozzarella", "Pineapple"], 10.00)
veggie = Pizza("Veggie", ["Tomato sauce", "Mozzarella", "Bell peppers", "Onions", "Mushrooms", "Olives"], 9.00)
four_cheese = Pizza("Four Cheese", ["Tomato sauce", "Mozzarella", "Cheddar", "Parmesan", "Blue cheese"], 11.50)
mexican = Pizza("Mexican", ["Tomato sauce", "Mozzarella", "Jalapenos", "Onions", "Bell peppers"], 11.00)
garden_fresh = Pizza("Garden Fresh", ["Tomato sauce", "Mozzarella", "Spinach", "Artichokes", "Cherry tomatoes"], 9.50)



restaurant = PizzaRestaurant("Gourmet Pizzeria", [margherita, hawaiian, veggie, four_cheese, mexican, garden_fresh])


restaurant.display_menu()

# restaurant.order_pizza("Pepperoni")
# restaurant.order_pizza("Seafood")
restaurant.order_pizza("Hawaiian")
# restaurant.order_pizza("Four Cheese")