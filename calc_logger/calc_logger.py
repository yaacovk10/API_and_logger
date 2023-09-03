import logging
from enum import Enum

class Actions(Enum):
    SUM = 0
    MULTIPLICATION = 1
    DIVISION = 2
    SUBTRACTION = 3

# Configure the logger to log to both console and a file
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='calculator.log')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(console_handler)

def menu():
    while True:
        for action in Actions:
            print(f"{action.value} - {action.name}")
        try:
            user_choice = Actions(int(input("Choose your action: ")))
            a = int(input("Insert 1st number: "))
            b = int(input("Insert 2nd number: "))
            
            if user_choice == Actions.SUM:
                result = a + b
                logger.info(f"Sum: {a} + {b} = {result}")
                print(f"Result: {a} + {b} = {result}")
            elif user_choice == Actions.SUBTRACTION:
                result = a - b
                logger.info(f"Subtraction: {a} - {b} = {result}")
                print(f"Result: {a} - {b} = {result}")
            elif user_choice == Actions.MULTIPLICATION:
                result = a * b
                logger.info(f"Multiplication: {a} * {b} = {result}")
                print(f"Result: {a} * {b} = {result}")
            elif user_choice == Actions.DIVISION:
                if b == 0:
                    logger.error("Division by zero is not allowed.")
                    print("Error: Division by zero is not allowed.")
                    continue
                result = a / b
                logger.info(f"Division: {a} / {b} = {result}")
                print(f"Result: {a} / {b} = {result}")
            else:
                logger.warning("Invalid choice. Please select a valid action.")
                print("Warning: Invalid choice. Please select a valid action.")
                continue

            return result
        except ValueError:
            logger.error("Invalid input. Please enter valid numbers and choices.")
            print("Error: Invalid input. Please enter valid numbers and choices.")
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            print(f"Error: An error occurred: {str(e)}")

if __name__ == '__main__':
    print(f"Result: {menu()}")
