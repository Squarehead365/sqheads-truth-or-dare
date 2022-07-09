import time
import random
from gen_base import generator_base



# def generate_ship(chosen_one = ""):
#     chosen_one = random.choice()

class term_gui_base():


    
    def question_dare(self, answer = ""):
        print("\ngenerate one more dare?")
        answer = input("type y to generate, type n to exit to main menu , or type q to exit from program: ")  
        if answer == "y":
            generator_base.generate_dare()
            self.question_dare()
        elif answer == "n":  
            print("\nthank for generating")
            print("redirecting to main menu...")
            self.menu()
            time.sleep(15)
        elif answer == "q":
            pass
        else:  
            print("sorry, you didnt type n, y or q, please type again") 
            self.question_dare()

    def question_truth(self, answer = ""):
        print("\ngenerate one more truth?")
        answer = input("type y to generate, type n to exit to main menu , or type q to exit from program: ")  
        if answer == "y":
            generator_base.generate_truth()
            self.question_truth()
        elif answer == "n":  
            print("\nthank for generating")
            print("redirecting to main menu...")
            self.menu()
            time.sleep(15)
        elif answer == "q":
            pass
        else:  
            print("sorry, you didnt type n, y or q, please type again") 
            self.question_dare()

    def menu(self, menu_choice = ""):
        print("\nwelcome to the main menu of the truth and dare (term gui version)!")
        menu_choice = input("type 1 for dare, type 2 for truth, and type q to exit from program: ")
        if menu_choice == "1":
            generator_base.generate_dare()
            self.question_dare()
        elif menu_choice == "1":
            generator_base.generate_truth()
            self.question_truth()
        elif menu_choice == "q":
            pass
        else:
            print("please type 1 or 2")
            self.menu()


tg = term_gui_base()
generator_base.general_dare_enable()
generator_base.general_truth_enable()
tg.menu()