from time import sleep

class Restaurant(object):
    def __init__(self, *args) -> None:
        # print(f"Restaurant.__init__: {args}")
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            print(f"Creating new Restaurant instance")
            cls._instance = super(Restaurant, cls).__new__(cls, *args, **kwargs)
            cls._instance._orders = 0
            cls._instance._total_sales = 0
        else:
            print("Using existing instance")
        return cls._instance

    def __str__(self) -> str:
        return f"{self._orders} orders were placed worth ${self._total_sales: .2f}"
    
    def order_food(self, food_type):
        food = Food.order_food(food_type)
        if food is not None:
            self._instance._orders += 1
            self._instance._total_sales += food.price()
            return food      

class Food():
    def __init__(self) -> None:
        # print(f"{type(self)} created in {__name__}")
        pass

    def price(self):
        return 0
    
    def prepare(self):
        pass

    def __str__(self) -> str:
        return f"{type(self).__name__}: $ {self.price()}"

    @staticmethod
    def order_food(food_type: str):
        food = None
        if isinstance(food_type, str):
            cleaned_food_type = food_type.strip().lower()
            if cleaned_food_type == "cheeseburger": food = Cheeseburger()
            elif cleaned_food_type == "pasta": food = Pasta()
            elif cleaned_food_type == "pizza": food = Pizza()
            else: print(f"{food_type} isnt on the menu, please order something else")
            if food is not None: 
                food.prepare()
                return food
        else:
            print("Please enter your order as a string.")
            return None

class Cheeseburger(Food):
    # def __str__(self):
    #     return f"{__class__.__name__}: ${self.price(): .2f}"
    
    def price(self):
        return 9.99
    
    def prepare(self):
        print("Cheeseburger: grilling meat patty")
        sleep(1) 
        print("Cheeseburger: adding cheese and toasting bun")
        sleep(1)
        print("Cheeseburger: Adding toppings and plating")
        sleep(1)
        print("Cheeseburger: All done!")


class Pasta(Food):
    # def __str__(self):
    #     return f"{__class__.__name__}: ${self.price(): .2f}"
    
    def price(self):
        return 12.99
    
    def prepare(self):
        print("Pasta: Boiling water and making sauce")
        sleep(1) 
        print("Pasta: Adding noodles to sauce")
        sleep(1) 
        print("Pasta: Coming right up!")

class Pizza(Food):
    # def __str__(self):
    #     return f"{__class__.__name__}: ${self.price(): .2f}"
    
    def price(self):
        return 5.99
    
    def prepare(self):
        print("Pizza: Placing pizza in the oven")
        sleep(1) 
        print("Pizza: Adding parmesan, pepper flakes and herbs")
        sleep(.5)
        print("Pizza: Pizza served!")

if __name__ == '__main__':
    r = Restaurant()
    food = r.order_food("Cheeseburger")
    if food:
        print(food)

    food = r.order_food("pasta")
    if food: print(food)

    food = r.order_food("pizza")
    if food: print(food)


    food = r.order_food("mac and cheese")
    if food: print(food)

    print(r)

    r2 = Restaurant()
    print(f"Does r2 == r? {r2 is r}, {r2}")

    
