class FishOrder:
    def order(self, *toppings):
        if len(toppings) == 0:
            print("Ordering Fried Fish.")
        elif len(toppings) == 1:
            print(f"Ordering a Fish with {toppings[0]}.")
        else:
            topping_list = ', '.join(toppings)
            print(f"Ordering a Fish with multiple toppings: {topping_list}.")

# Using the class
customer = FishOrder()

customer.order()                        
customer.order("Lemon")             
customer.order("Lemon", "olives")   
