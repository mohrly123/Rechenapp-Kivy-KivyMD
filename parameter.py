from kivy.properties import NumericProperty
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
import random as rnd


class Startseite(MDScreen):
    pass
    
class Suchaufgaben(MDScreen):
    pass
    
class PlusMinusRechnungen(MDScreen):
    def __init__(self, **kwargs):
        super(PlusMinusRechnungen, self).__init__(**kwargs)
        self.counter_richtig = 0
        self.counter_falsch = 0
    
    def click_start(self):
        # Start Button verschwinden lassen
        self.ids.startbtn.opacity = 0
        self.ids.startbtn.disabled = True
        self.ids.eingabe.opacity = 1
        self.ids.check.opacity = 1
        self.ids.counter_right.opacity = 1
        self.ids.counter_false.opacity = 1
        self.programm()
        
    def click_close(self):
        # Start Button wieder aktiv machen
        self.ids.startbtn.opacity = 1
        self.ids.startbtn.disabled = False
        self.ids.rechnung_label.opacity = 0
        self.ids.eingabe.opacity = 0
        self.ids.richtig.text = ''  # Hinweis: Rücksetzung des Labels

    def programm(self):
        self.ids.rechnung_label.opacity = 1
        num1 = rnd.randint(1, 50)
        num2 = rnd.randint(1, 50)
        operator = rnd.choice(["+", "-"])
        
        if operator == "+":
            self.ids.rechnung_label.text = f'Wie viel ist {num1} {operator} {num2}?'
            self.ergebnis = num1 + num2
        elif operator == "-":
            hight = max(num1, num2)
            low = min(num1, num2)
            self.ids.rechnung_label.text = f'Wie viel ist {hight} {operator} {low}?'
            self.ergebnis = hight - low
            
        self.ids.richtig.text = ''  # Reset des Labels beim neuen Programm

    def check_answer(self):
        try:
            if int(self.ids.eingabe.text) == self.ergebnis:
                self.counter_richtig += 1
                self.ids.eingabe.text = ''  # Fehler hier korrigiert
           
                self.programm()
                self.ids.eingabe.line_color_normal = 'green'
                self.ids.eingabe.line_color_focus = "green"
                self.ids.counter_right.text = f'Richtig: {self.counter_richtig}'
            else:
                self.counter_falsch += 1
                self.ids.eingabe.line_color_normal = 'red'
                self.ids.eingabe.line_color_focus = 'red'
                self.ids.eingabe.text = ''  # Fehler hier korrigiert
                self.ids.counter_false.text = f'Falsch: {self.counter_falsch}'
        except ValueError:
            self.ids.richtig.text = 'Leere Eingabe'


class MainApp(MDApp):
    def build(self):
        return Builder.load_file("testapp.kv")


MainApp().run()
