from cgitb import enable
import time
import random
from gen_base import generator_base


class term_gui_base():


    

    def menu(self, menu_choice = ""):
        print("\nвітаємо в головному меню правди і дії!")
        menu_choice = input('напишіть "1" для дії, напишіть "2" для правди, напишіть "q" щоби вийти з гри, або напишіть "r" щоби в меню включення\виключення категорій: ')
        if menu_choice == "1":
            generator_base.generate_dare()
            self.menu()
        elif menu_choice == "2":
            generator_base.generate_truth()
            self.menu()
        elif menu_choice == "q":
            pass
        elif menu_choice == "r":
            self.enable_disable_menu()
        else:
            print("будь ласка напишіть 1, 2, r або q")
            

    def enable_disable_menu(self):
        print("\nвітаємо в меню включення\виключення категогрій. зараз в нас є:\n1: категорія фандому\персонажів\n2: категорія обіймів\nm: повернутися до меню")
        print('(ради стабільності програми, існує ще одна прихована категорія під назвою "основна". її основна задача - не дати користувачу згенерувати пустий лист, через те що це викличе фатальну помилку)')
        enable_disable_menu_choice = input('введіть номер перед назвою категорії яку ви хочете налаштуватиб або введіть "m" щоби вернутися до меню: ')
        if enable_disable_menu_choice == "1":
            self.character_fandom_submenu()
        if enable_disable_menu_choice == "2":
            self.hugsncuddles_submenu()
        if enable_disable_menu_choice == "m":
            self.menu()
        
    
    def character_fandom_submenu(self):
        print("чотири дії доступні:")
        print("1: включити дію\n2: включити правду\n3: виключити правду\n4: виключити дію")
        character_fandom_submenu_choice = input("введіть номер дії: ")
        if character_fandom_submenu_choice == "1":
            generator_base.creative_dare_enable()
            self.enable_disable_menu()
        if character_fandom_submenu_choice == "2":
            generator_base.creative_truth_enable()
            self.enable_disable_menu()
        if character_fandom_submenu_choice == "3":
            generator_base.creative_dare_disable()
            self.enable_disable_menu()
        if character_fandom_submenu_choice == "4":
            generator_base.creative_truth_enable()
            self.enable_disable_menu()
        
        else:
            print("будь ласка напишіть 1, 2, 3, чи 4")

    def hugsncuddles_submenu(self):
        print("дві дії доступні:")
        print("1: включити дію\n2: виключити дію: ")
        character_fandom_submenu_choice = input("введіть номер дії: ")
        if character_fandom_submenu_choice == "1":
            generator_base.hugs_n_cuddles_dare_enable()
            self.enable_disable_menu()
        if character_fandom_submenu_choice == "2":
            generator_base.hugs_n_cuddles_dare_disable()
            self.enable_disable_menu()
        else: 
            print("будь ласка напишіть 1, 2")


         
        


tg = term_gui_base()
generator_base.general_dare_enable()
generator_base.general_truth_enable()
tg.menu()