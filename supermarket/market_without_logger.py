from enum import Enum

supermarket_products = [
    {"index": 1, "product": "Apples", "price": 1.99, "units_in_stock": 50},
    {"index": 2, "product": "Bananas", "price": 0.59, "units_in_stock": 30},
    {"index": 3, "product": "Milk", "price": 2.49, "units_in_stock": 20},
    {"index": 4, "product": "Bread", "price": 1.89, "units_in_stock": 15},
    {"index": 5, "product": "Eggs", "price": 2.99, "units_in_stock": 40}
]



class Actions (Enum):
    DISPLAY_PRODUCTS = 0 
    ADD_PRODUCT_TO_CART = 1
    PRINT_YOUR_CART =2
    EXIT = 99
   

class Cart():
    def __init__(self) -> None:
        self.cart =[]
        

    def add_product(self):
        display_products()
        index = int(input("Choose the index product to add: "))
        amount = int(input("How much you want: "))
        product = supermarket_products[index -1]['product']
        amount = update_stock(index, amount)
        self.update_cart(product, amount)

    def update_cart(self,  product, amount):
        if amount:
            found = False
            for item in self.cart:
                if item['product'] == product: 
                    item['amount']+= amount
                    found = True
            if not found: self.cart.append({"product": product, "amount": amount})




def update_stock(index, amount):
    stock = int(supermarket_products[index -1]['units_in_stock'])
    if stock>= amount: 
        supermarket_products[index -1]['units_in_stock'] -= amount
        print(f"{amount} units of {supermarket_products[index -1]['product']} added to your cart.")
        available_amount = amount
    else:
        print(f"Only {stock} units of {supermarket_products[index -1]['product']} in stock.")
        print(f"{stock} units of {supermarket_products[index -1]['product']} added to your cart.")
        available_amount = stock
    return available_amount
    

def display_products():
    # Print keys of each item
    keys = list(supermarket_products[0].keys())  # Assuming all items have the same keys
    print("\t".join(keys))

    # Print values of each item
    for product in supermarket_products:
        values = list(product.values())
        print("\t".join(map(str, values[:])))  # Exclude the index value

    


def menu():
    cart = Cart()
    while (True):
        print("Welcome to  our supermarket")
        for action in Actions:
            print(f"{action.value} -  {action.name}")
        print("Insert your selection : ")
        user_choice =Actions(int(input("")))
        if user_choice == Actions.DISPLAY_PRODUCTS:display_products()
        if user_choice == Actions.ADD_PRODUCT_TO_CART:cart.add_product()
        if user_choice == Actions.PRINT_YOUR_CART:print(cart.cart)
        if user_choice == Actions.EXIT:return
        


if __name__ == '__main__':
    print("start")

    menu()