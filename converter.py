from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatButton,MDFillRoundFlatIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar

class ConverterApp(MDApp):
    def flip(self):
        if self.state==0:
            self.state=1
            self.toolbar.title="Decimal to Binary"
            self.input.text="Enter a Decimal Number :"

        else :
            self.state=0
            self.toolbar.title="Binary to Decimal"
            self.input.text="Enter a Binary Number :"
        self.converter.text=""
        self.label.text=""

    
    def convert(self, args):
        if self.state==0:
            val=str(int(self.input.text,2))
            self.label.text="In decimal is :"
        else :
            val=bin(int(self.input.text))[2:]
            self.label.text="In Binary is :"
        self.converter.text=val


    def build(self):
        self.state=0
        screen=MDScreen()
        self.toolbar = MDTopAppBar(title="Binary To Decimal")
        self.toolbar.pos_hint={"top":1}
        self.toolbar.right_action_items =[
            ["rotate-3d-variant",lambda x:self.flip()]
        ]
        screen.add_widget(self.toolbar)
        
        #icon
        screen.add_widget(Image(source="logo.png",
        pos_hint={"center_x": 0.5,"center_y": 0.7}
        ))

        #input
        self.input=MDTextField(
            halign="center",
            size_hint=(0.8,1),
            pos_hint = {"center_x": 0.5, "center_y": 0.5},
            font_size=22
        
        )
        screen.add_widget(self.input)

        #secondary primary label
        self.label=MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y": 0.35},
            theme_text_color="Secondary"

        )
        self.converter=MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y": 0.3},
            theme_text_color="Primary",
            font_style="H5"

        )
        screen.add_widget(self.label)
        screen.add_widget(self.converter)

        #button
        screen.add_widget(MDFillRoundFlatButton(
            text="Convert",
            font_size=17,
            pos_hint = {"center_x": 0.5, "center_y": 0.15},
            on_press=self.convert
        ))
        



        return screen

if __name__=='__main__':
    ConverterApp().run()