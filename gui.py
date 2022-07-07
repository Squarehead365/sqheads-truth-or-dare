from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton, MDRoundFlatButton
from kivymd.uix.toolbar import MDToolbar
from gen_base import *
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDSwitch
from kivy.uix.behaviors import ButtonBehavior







chosen_one= "press genration buttons to change this label"



class truthordareApp(MDApp):
    def build(self):

        screen = MDScreen()
        self.toolbar = MDToolbar(title="truth or dare")
        self.toolbar.pos_hint ={"top": 1}
        screen.add_widget(self.toolbar)

        self.genoutput = MDLabel(text=chosen_one, text_color=(0,0,0,1))
        self.genoutput.pos_hint = {"center_x": 0.6, "center_y": 0.8,}

        screen.add_widget(self.genoutput)
        self.daregenbutn = MDFillRoundFlatButton(text="dare")
        self.daregenbutn.pos_hint = {"center_x": 0.5, "center_y": 0.6}
        screen.add_widget(self.daregenbutn)

        self.truthgenbutn = MDFillRoundFlatButton(text="truth")
        self.truthgenbutn.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        screen.add_widget(self.truthgenbutn)

        self.creativedarelabel = MDLabel(text="creative dare")
        self.creativedarelabel.pos_hint = {"center_x": 1, "center_y": 0.4}
        screen.add_widget(self.creativedarelabel)

        self.creativedarecheckbox = MDSwitch()
        self.creativedarecheckbox.pos_hint = {"center_x": 0.4, "center_y": 0.4}
        screen.add_widget(self.creativedarecheckbox)

        self.creativetruthlabel = MDLabel(text="creative truth")
        self.creativetruthlabel.pos_hint = {"center_x": 1, "center_y": 0.3}
        screen.add_widget(self.creativetruthlabel)


        self.creativetruthcheckbox = MDSwitch()
        self.creativetruthcheckbox.pos_hint = {"center_x": 0.4, "center_y": 0.3}
        screen.add_widget(self.creativetruthcheckbox)

        self.hugsncuddlesdarelabel = MDLabel(text="hugs n cuddles")
        self.hugsncuddlesdarelabel.pos_hint = {"center_x": 1, "center_y": 0.2}
        screen.add_widget(self.hugsncuddlesdarelabel)

        self.hugsncuddlesdarecheckbox = MDSwitch()
        self.hugsncuddlesdarecheckbox.pos_hint = {"center_x": 0.4, "center_y": 0.2}
        screen.add_widget(self.hugsncuddlesdarecheckbox)
        return screen
        

if __name__ == '__main__':
    truthordareApp().run()