# Burger ingredients and prices
ingredients = {
    "Bun": 1.00,
    "Beef Patty": 5.00,
    "Chicken Patty": 5.00,
    "Fish Patty": 6.00,
    "Veggie Patty": 4.00,
    "Extra Patty": 8.00,
    "American Cheese Slice": 1.00,
    "Cheddar Cheese Slice": 1.00,
    "Swiss Cheese Slice": 1.50,
    "Avocado": 2.50,
    "Egg": 2.00,
    "Crisp Onion": 1.00,
    "Caramelized Onion": 1.50,
    "Raw Onion": 0.50,
    "Lettuce": 0.50,
    "Coleslaw": 1.00,
    "Pickled Cucumber": 0.50,
    "Sweet Relish": 1.00,                        
    "Tomato Slices": 0.70,                        
    "BBQ Sauce": 0.50,
    "Special Sauce": 0.50,
    "Mayo": 0.20
}

# Beverage options and prices
beverages = {
    "Soda": 3.00,
    "Juice": 4.00,
    "Energy Drink": 6.00,
    "Beer": 8.00,
    "Milkshake": 8.00
}

def take_order():
    burger_ingredients = []
    print("Welcome to our burger shop!")
    print("Here's a list of our burger ingredients and prices:")
    for ingredient, price in ingredients.items():
        print(f"{ingredient}: ${price}")
    print("Let's start building your burger!")
    while True:
        ingredient = input("Enter an ingredient (press enter when finished): ")
        if not ingredient:
            break
        if ingredient not in ingredients:
            print("Sorry, that's not a valid ingredient.")
        else:
            burger_ingredients.append(ingredient)
    return burger_ingredients

def get_beverage():
    while True:
        answer = input("Would you like a beverage? (yes/no) ")
        if answer.lower() == "yes":
            print("Great! Here are our beverage options:")
            for beverage, price in beverages.items():
                print(f"{beverage}: ${price}")
            while True:
                beverage_choice = input("What beverage would you like? ")
                if beverage_choice not in beverages:
                    print("Sorry, that's not a valid beverage choice.")
                else:
                    return beverage_choice
        elif answer.lower() == "no":
            print("No problem, let's continue with your burger order.")
            return None
        else:
            print("Sorry, I didn't understand your answer.")

def calculate_total_price(burger_ingredients, beverage_choice=None):
    total_price = 0
    for ingredient in burger_ingredients:
        total_price += ingredients[ingredient]
    if beverage_choice:
        total_price += beverages[beverage_choice]
    return total_price

def main():
    burger_ingredients = take_order()
    beverage_choice = get_beverage()
    total_price = calculate_total_price(burger_ingredients, beverage_choice)
    print(f"Your burger with {', '.join(burger_ingredients)} {'and ' + beverage_choice if beverage_choice else ''} costs ${total_price:.2f}.")

if __name__ == "__main__":
    main()
