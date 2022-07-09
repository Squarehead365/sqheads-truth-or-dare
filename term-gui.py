import time
import random
from gen_base import generator_base



# def generate_ship(chosen_one = ""):
#     chosen_one = random.choice()

class term_gui_base():


    

    def menu(self, menu_choice = ""):
        print("\nwelcome to the main menu of the truth and dare (term gui version)!")
        menu_choice = input("type 1 for dare, type 2 for truth, and type q to exit from program: ")
        if menu_choice == "1":
            generator_base.generate_dare()
            self.menu()
        elif menu_choice == "2":
            generator_base.generate_truth()
            self.menu()
        elif menu_choice == "q":
            pass
        else:
            print("please type 1 or 2")
            self.menu()


tg = term_gui_base()
generator_base.general_dare_enable()
generator_base.general_truth_enable()
tg.menu()