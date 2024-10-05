from kivy.core.window import Window
from kivy.config import Config
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.clock import Clock
import random


class Startseite(MDScreen):
    pass
        

class PlusMinus(MDScreen):
    def start(self):                            # startet die start_btn methode mit 0.2 sek verzögerung
        Clock.schedule_once(self.start_btn, 0.2)
    
    def start_btn(self, dt):                    # Methode um den Startbtn zu verstecken und das eigentliche Programm zu starten
        self.ids.start.opacity = 0              # Start Button verstecken
        self.ids.start.disabled = True          # Start Button deaktivieren
        self.ids.willkommen_label.opacity = 1   # Willkommen Label auf sichtbar setzen
        self.ids.rechnung.opacity = 1           # Rechnung auf Sichtbar setzen
        self.ids.btn1.opacity = 1               # btn1 auf sichtbar
        self.ids.btn2.opacity = 1               # btn2 auf sichtbar
        self.ids.btn3.opacity = 1               # btn3 auf sichtbar
        self.rechnung_erstellen()

    def close(self):                            # startet die close_btn methode mit 0.2 sek verzögerung
        Clock.schedule_once(self.close_btn, 0.2)
    
    def close_btn(self, dt):                    # Methode um den Startbtn sichtbar zu machen und das eigentliche Programm zu schließen
        self.ids.start.opacity = 1              # Start Button anzeigen
        self.ids.start.disabled = False         # Start Button aktivieren
        self.ids.willkommen_label.opacity = 0   # Willkommen Label auf unsichtbar setzen
        self.ids.rechnung.opacity = 0           # Rechnung auf unsichtbar setzen
        self.ids.btn1.opacity = 0               # btn1 auf unsichtbar
        self.ids.btn2.opacity = 0               # btn2 auf unsichtbar
        self.ids.btn3.opacity = 0               # btn3 auf unsichtbar

    def rechnung_erstellen(self):               # Logik um eine Rechnung zu bauen
        try:
            rdnum1 = random.randint(1,50)           # Random Nummer1 zw 1 und 50 
            rdnum2 = random.randint(1,50)           # Random Nummer2 zw 1 und 50
            while rdnum1 == rdnum2:                 # Sollte Num 1 und Num2 gleich sein, werden neue Nummern generiert
                rdnum1 = random.randint(1,50)
                rdnum2 = random.randint(1,50)

            lownum = min(rdnum1, rdnum2)             # Aus Nummer 1 und Nummer 2 die niedrigere
            highnum = max(rdnum1, rdnum2)            # Aus Nummer 1 und Nummer 2 die höhere
            operator = random.choice(["+", "-"])     # Hier wird zufällig aus + oder - gewählt
            
            if operator == "+":                     # Wenn der Operator Plus ist
                self.ergebnis = lownum + highnum    # Ist das Ergebnis kleine + hohe Nummer
                reihenfolge = random.choice([f"Wie viel ist {lownum} {operator} {highnum}?", f"Wie viel ist {highnum} {operator} {lownum}?"])
                self.ids.rechnung.text = reihenfolge
            elif operator == "-":                   # Wenn der Operator Minus ist
                self.ergebnis = highnum - lownum    # Ist das Ergebnis hohe - kleine Nummer
                self.ids.rechnung.text = f"Wie viel ist {highnum} {operator} {lownum}?"

            falsche_antwort1 = self.ergebnis + random.randint(1,10)  # 1. Falsche Antwort bauen
            falsche_antwort2 = self.ergebnis - random.randint(1,10)  # 2. Falsche Antwort bauen
            falsche_antwort2 = abs(falsche_antwort2)                 # Das keine negative Zahl entsteht

            while falsche_antwort1 == self.ergebnis or falsche_antwort1 == falsche_antwort2:
                falsche_antwort1 = self.ergebnis + random.randint(1, 10)
        
            while falsche_antwort2 == self.ergebnis or falsche_antwort2 == falsche_antwort1:
                falsche_antwort2 = self.ergebnis - random.randint(1, 10)
                falsche_antwort2 = abs(falsche_antwort2)

            antworten = [falsche_antwort2, falsche_antwort1, self.ergebnis] # Eine Liste mit den Antworten bauen
            random.shuffle(antworten)                                      # Durchmischen der Antworten

            # Weisen den Buttons die Antworten zu
            self.ids.btn1.text = str(antworten[0])              # Auf den ersten Wert in der Liste zugreifen
            self.ids.btn2.text = str(antworten[1])              # Auf den zweiten Wert in der Liste zugreifen
            self.ids.btn3.text = str(antworten[2])              # Auf den dritten Wert in der Liste zugreifen

        except ValueError:
            print("ERROR")

    
    def check_answer(self, button_text):
        # Prüfe, ob die gewählte Antwort richtig ist
        if int(button_text) == self.ergebnis:
            print("Richtige Antwort!")
            self.ids.willkommen_label = "Richtige Antwort!"
            self.rechnung_erstellen()
        else:
            print("Falsche Antwort!")
            self.willkommen_label = "Falsche Antwort!"


class Myyapp(MDApp):
    def build(self):
        #Window.size = (411,731)
        #Config.set('graphics', 'dpi', '160')
        return Builder.load_file("desi.kv")
    
if __name__ == "__main__":
    Myyapp().run()
