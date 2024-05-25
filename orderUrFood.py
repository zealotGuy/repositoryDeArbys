total_cost = 0
food_order = []
menu = {
    "chicken_sand": 5.25,
    "beef_sand": 6.25,
    "tofu_sand": 5.75,
    "s_drink": 1.00,
    "m_drink": 1.75,
    "l_drink": 2.25,
    "s_fries": 1.00,
    "m_fries": 1.50,
    "l_fries": 2.00,
    "ketchup": 0.25
}

print("Welcome to Arbys Mini! What would you like to order?")
for food, price in menu.items():
    print(f"{food.capitalize()}: ${price}")

for food in menu:
  user_choice = input(f"Do you want a {food}? (yes/no) ").lower()
  while user_choice != "yes" and user_choice != "no":
    print("hey now you didnt do it properly do it again")
    user_choice = input("Do you want a" + food + "? (yes/no) ").lower()
  if user_choice == "yes":
    while True:
        amounts = input("How many??")
        if amounts.isdigit() and int(amounts) >= 0:
            break
        print("enter a number por favor")
    total_cost += menu[food] * int(amounts)
    food_order.append((food, int(amounts)))

print("ur order:")

for food, amounts in food_order:
    print(f"{amounts} {food}")
    
print("The total is going to be $" + str(total_cost))

while True:
    edit_order = input("So, now that we r here, do you want to edit your order?? (add/remove/done): ").lower()
    if edit_order == "done":
        break
    elif edit_order == "add":
        food = input("What do u wanna add?").lower()
        if food in menu:
            while True:
                amounts = input("how much?")
                if amounts.isdigit() and int(amounts) >= 0:
                    total_cost += menu[food] * int(amounts)
                    food_order.append((food, int(amounts)))
                    break
                print("numbers plss")
        else:
            print("what you are asking for doesn't exist, if you want that go to another store .-.")
   
    elif edit_order == "remove":
        if not food_order:
            print("you do NOT have an order .-.")
        else:
            print("current order:")
            for i, (food, amounts) in enumerate(food_order):
                print(f"{i + 1}. {amounts} {food}")
            index = input("Which number do you want to remove from ur order?")
            if index.isdigit():
                index = int(index) - 1
                if 0 <= index < len(food_order):
                    food, amounts = food_order.pop(index)
                    total_cost -= menu[food] * amounts
                    print("Removed.")
                else:
                    print("numbers plsss")
            else:
                print("numbers por favor")

print("ur order:")

for food, amounts in food_order:
    print(f"{amounts} {food}")
print("Total: $" + str(total_cost))
