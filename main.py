"""
Programa MyDiary
Analista:
Objetivo: teste ywefyduystdfuyst
Revisoon Date:

"""


from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

class testApp(Screen):
    def __init__(self,**Kwargs):
        super().__init__(**Kwargs)

    pass
class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepOrange"


        return testApp()
if __name__=="__main__":
    Window.size=(360,640)
    Builder.load_file("tela.kv")
    MyApp().run()

