from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton, MDRoundFlatButton
from kivymd.uix.toolbar import MDToolbar
from gen_base import *
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDSwitch
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty




class disable_enable_category():
        def enable_creative_category(self):
            generator_base.creative_dare_enable(self)
            generator_base.creative_truth_enable(self)

        def disable_creative_category(self):
            generator_base.creative_dare_disable(self)
            generator_base.creative_truth_disable(self)

        

genoutput = """
MDLabel:
    id: output_id
    text: "sus"
    theme_text_color: "Custom"
    text_color: 0, 0, 0, 1
    pos_hint: {"center_x": 0.6, "center_y": 0.8}
    """

    
            





 




class truthordareApp(MDApp):



            


    
            
  
    def build(self):
        pass
        # global output_text


        # class Lablechange():
        
        #     def labelchange_dare(self):
        #         global output_text
        #         global the_chosen_one
        #         generator_base.generate_dare(self)
        #         self.output_text = the_chosen_one

        



        screen = MDScreen()
        self.toolbar = MDToolbar(title="truth or dare")
        self.toolbar.pos_hint ={"top": 1}
        screen.add_widget(self.toolbar)

        self.genoutput = MDLabel(text= "test", text_color=(0,0,0))
        self.genoutput.pos_hint = {"center_x": 0.6, "center_y": 0.8,}
        screen.add_widget(self.genoutput)

        



        self.daregenbutn = MDFillRoundFlatButton(text="dare")
        self.daregenbutn.pos_hint = {"center_x": 0.5, "center_y": 0.6}
        screen.add_widget(self.daregenbutn)

        self.truthgenbutn = MDFillRoundFlatButton(text="truth", on_press= generator_base.generate_truth)
        self.truthgenbutn.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        screen.add_widget(self.truthgenbutn)

        creative_enable_butn = MDFillRoundFlatButton(text="creative enable", on_press=disable_enable_category.enable_creative_category)
        creative_enable_butn.pos_hint = {"center_x": 0.5, "center_y": 0.4}
        screen.add_widget(creative_enable_butn)

        creative_disable_butn = MDFillRoundFlatButton(text="creative disable", on_press=disable_enable_category.disable_creative_category)
        creative_disable_butn.pos_hint = {"center_x": 0.5, "center_y": 0.3}
        screen.add_widget(creative_disable_butn)
        

        hugsncuddles_enable_butn = MDFillRoundFlatButton(text="sus", on_press=generator_base.hugs_n_cuddles_dare_enable)
        hugsncuddles_enable_butn.pos_hint = {"center_x": 0.5, "center_y": 0.2}
        screen.add_widget(hugsncuddles_enable_butn)

        hugsncuddles_disable_butn = MDFillRoundFlatButton(text="sus", on_press=generator_base.hugs_n_cuddles_dare_disable)
        hugsncuddles_disable_butn.pos_hint = {"center_x": 0.5, "center_y": 0.1}
        screen.add_widget(hugsncuddles_disable_butn)

        generator_base.general_dare_enable(self)
        generator_base.general_truth_enable(self)



        return screen
        

if __name__ == '__main__':
    truthordareApp().run()