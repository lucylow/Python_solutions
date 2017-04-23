




#Shopping Cart example


# shopping cart class - creating shopping cart objects 

class ShoppingCart(object):
    
    
    items_in_cart = {}
    
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        # method to add product to the cart.
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        # method to remove product from the cart.
        if product in self.items_in_cart:
            del self.items_in_cart[product] # delete from list 
            print product + " removed."
        else:
            print product + " is not in the cart."
            

# create instance 

my_cart = ShoppingCart("Lucy")
my_cart.add_item("apples",2)







# Inheritence 


class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()




