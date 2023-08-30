from enum import Enum

class Actions(Enum):
    SUM= 0
    MULTIPLICATION = 1
    DIVISION = 2

def menu():
    while (True):

        for action in Actions:
            print(f"{action.value} - {action.name}")
        user_choice = Actions(int(input("choose your action : ")))
        a = int(input("insert 1st number: "))
        b = int(input("insert 2nd number: "))
        if user_choice == Actions.SUM: return a + b
        if user_choice == Actions.MULTIPLICATION: return a * b
        if user_choice == Actions.DIVISION: return a / b


if __name__ == '__main__':
    print(f"result : {menu()}")