import logging
from enum import Enum

# Configure the logging settings
logging.basicConfig(filename='supermarket.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

supermarket_products = [
    {"index": 1, "product": "Apples", "price": 1.99, "units_in_stock": 50},
    {"index": 2, "product": "Bananas", "price": 0.59, "units_in_stock": 30},
    {"index": 3, "product": "Milk", "price": 2.49, "units_in_stock": 20},
    {"index": 4, "product": "Bread", "price": 1.89, "units_in_stock": 15},
    {"index": 5, "product": "Eggs", "price": 2.99, "units_in_stock": 40}
]

class Actions(Enum):
    DISPLAY_PRODUCTS = 0
    ADD_PRODUCT_TO_CART = 1
    PRINT_YOUR_CART = 2
    EXIT = 99

class UserInterface:
    def __init__(self, cart):
        self.cart = cart
        self.exit_flag = False  # Added exit_flag to control the loop


    def display_menu(self):
        # Display the menu options and handle user input
        logging.info("Displaying menu options.")
        print("Welcome to our supermarket")
        for action in Actions:
            print(f"{action.value} - {action.name}")
        print("Insert your selection: ")
        try:
            user_choice = Actions(int(input("")))
            if user_choice == Actions.DISPLAY_PRODUCTS:
                logging.info("User selected to display products.")
                self.display_products()  # Call the local method to display products
            elif user_choice == Actions.ADD_PRODUCT_TO_CART:
                logging.info("User selected to add a product to the cart.")
                self.cart.add_product()
            elif user_choice == Actions.PRINT_YOUR_CART:
                logging.info("User selected to print the cart.")
                print(self.cart.get_cart())
            elif user_choice == Actions.EXIT:
                logging.info("User selected to exit the program.")
                self.exit_flag = True  # Set the exit flag to True
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            logging.error("Invalid input. User entered an invalid choice.")
            print("Invalid input. Please enter a valid choice.")

    def display_products(self):
        # Display the list of supermarket products
        # Print keys of each item
        logging.info("Displaying supermarket products.")

        keys = list(supermarket_products[0].keys())  # Assuming all items have the same keys
        print("\t".join(keys))

        # Print values of each item
        for product in supermarket_products:
            values = list(product.values())
            print("\t".join(map(str, values[:])))  # Exclude the index value

class Cart:
    def __init__(self):
        self.cart = []

    def add_product(self):
        # Add the product to the cart
        self.display_products()
        try:
            index = int(input("Choose the index product to add: "))
            amount = int(input("How much do you want: "))
            product = supermarket_products[index - 1]['product']
            amount = update_stock_and_return_available_amount(index, amount)
            self.update_cart(product, amount)
        except (ValueError, IndexError):
            logging.error(f"Invalid input. User entered an invalid index: {index} or amount: {amount}.")
            print("Invalid input. Please enter a valid index and amount.")

    def update_cart(self, product, amount):
        # Update the cart based on the selected product and amount
        if amount:
            found = False
            for item in self.cart:
                if item['product'] == product:
                    item['amount'] += amount
                    found = True
            if not found:
                self.cart.append({"product": product, "amount": amount})

    def get_cart(self):
        # Return the current cart contents
        return self.cart

    def display_products(self):
        # Display the list of supermarket products
        logging.info("Displaying supermarket products.")
        UserInterface.display_products(self)  # Call the display_products method from UserInterface

def update_stock_and_return_available_amount(index, amount):
    stock = int(supermarket_products[index - 1]['units_in_stock'])
    if stock >= amount:
        supermarket_products[index - 1]['units_in_stock'] -= amount
        logging.info(f"{amount} units of {supermarket_products[index - 1]['product']} added to your cart.")
        print(f"{amount} units of {supermarket_products[index - 1]['product']} added to your cart.")
        available_amount = amount
    else:
        logging.error(f"User choose {amount} while only {stock} units of {supermarket_products[index - 1]['product']} in stock.")
        logging.info(f"{stock} units of {supermarket_products[index - 1]['product']} added to your cart.")
        print(f"Only {stock} units of {supermarket_products[index - 1]['product']} in stock.")
        print(f"{stock} units of {supermarket_products[index - 1]['product']} added to your cart.")
        available_amount = stock
    return available_amount

def menu(cart):
    ui = UserInterface(cart)
    while not ui.exit_flag:  # Use the exit flag to control the loop
        ui.display_menu()

if __name__ == '__main__':
    cart = Cart()
    menu(cart)
