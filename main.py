
from kivy.core.window import Window
from kivy.config import Config
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager

class Startseite(MDScreen):
    pass
        

class PlusMinus(MDScreen):
    pass

class Myyapp(MDApp):
    def build(self):
        #Window.size = (411,731)
        #Config.set('graphics', 'dpi', '160')
        return Builder.load_file("desi.kv")
    
if __name__ == "__main__":
    Myyapp().run()
