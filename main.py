from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
profit =0
menu_u = Menu()

coffeemaker = CoffeeMaker()
my_money_machine=MoneyMachine() 

is_on=True
while is_on:
    choice =input(f"what you like to drink?({menu_u.get_items()}). ")
    if choice=="off":
        is_on=False
    elif choice=='report':
       coffeemaker.report()
       my_money_machine.report()
    else:
        drink=menu_u.find_drink(choice)

        if coffeemaker.is_resource_sufficient(drink) and  my_money_machine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)






