from calculator import add, subtract, multiply, divide

def main():
    while True:
        print("Варіанти:")
        print("Введіть 'add', щоб додати два числа")
        print("Введіть 'subtract', щоб відняти два числа")
        print("Введіть 'multiply', щоб перемножити два числа")
        print("Введіть 'divide', щоб розділити два числа")
        print("Введіть 'quit', щоб завершити програму")
        
        user_input = input(": ")

        if user_input == "quit":
            break
        elif user_input in ("add", "subtract", "multiply", "divide"):
            try:
                num1 = float(input("Введіть перше число: "))
                num2 = float(input("Введіть друге число: "))
            except ValueError:
                print("Неправильний ввід. Будь ласка, введіть числові значення.")
                continue

            if user_input == "add":
                print(f"В результаті ми отримали {add(num1, num2)}")
            elif user_input == "subtract":
                print(f"В результаті ми отримали {subtract(num1, num2)}")
            elif user_input == "multiply":
                print(f"В результаті ми отримали {multiply(num1, num2)}")
            elif user_input == "divide":
                try:
                    print(f"В результаті ми отримали {divide(num1, num2)}")
                except ValueError as e:
                    print(e)
        else:
            print("Невідомий вхід")

if __name__ == "__main__":
    main()
