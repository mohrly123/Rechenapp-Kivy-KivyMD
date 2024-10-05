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
    def __init__(self,**kwargs):
        super(PlusMinus, self).__init__(**kwargs)
        self.counter_R = 0                      # Den Counter für die Richtigen erstellen
        self.counter_F = 0                      # Den Counter für die Falschen erstellen
    
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
        self.ids.btn1.disabled = False          # btn1 aktivieren
        self.ids.btn2.disabled = False          # btn2 aktivieren
        self.ids.btn3.disabled = False          # btn3 aktivieren
        self.ids.card_counter.opacity = 1       # Card beim betreten aktivieren
        self.ids.card_counter.disabled = False  # Card aktivieren
        self.ids.label_richtige.opacity = 1     # Label Counter Richtige aktivieren
        self.ids.label_falsche.opacity = 1      # Label Counter Falsche aktivieren
        
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
        self.ids.btn1.disabled = True           # btn1 deaktivieren
        self.ids.btn2.disabled = True           # btn 2 deaktivieren
        self.ids.btn3.disabled = True           # btn 3 deaktivieren
        self.ids.card_counter.opacity = 0       # Card beim betreten deaktivieren
        self.ids.card_counter.disabled = True   # Card deaktivieren
        self.ids.label_richtige.opacity = 0     # Label Counter Richtige deaktivieren
        self.ids.label_falsche.opacity = 0      # Label Counter Falsche deaktivieren
        self.counter_R = 0                      # Beim Closen den Counter auf 0 setzten
        self.ids.label_richtige.text = f"Richtige: {self.counter_R}"        # Den Text auch wieder auf 0 setzen
        self.counter_F = 0                      # Beim Closen den Counter auf 0 setzten
        self.ids.label_falsche.text = f"Falsche: {self.counter_F}"          # Den Text auch wieder auf 0 setzen
        self.ids.willkommen_label.text = "Willkommen zurück!"               # Nach dem Widerbetreten den Text anzeigen
        self.ids.willkommen_label.color = "orange"                          # Nach dem Wiederbetreten die Farbe auf orange setzen

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
    # Überprüfen, ob button_text nicht leer ist und eine Zahl darstellt
        if button_text.isdigit():
            if int(button_text) == self.ergebnis:
                self.counter_R += 1  # Counter für die richtigen um 1 erhöhen
                self.ids.label_richtige.text = f"Richtige: {self.counter_R}"
                self.ids.willkommen_label.text = "Richtige Antwort!"
                self.ids.willkommen_label.color = [0, 1, 0, 1]  # Setze die Farbe des Textes auf Grün
                self.rechnung_erstellen()  # Wenn die Antwort richtig war, eine neue Rechnung erstellen
            else:
                self.ids.willkommen_label.text = "Falsche Antwort!"
                self.counter_F += 1  # Counter für die falschen um 1 erhöhen
                self.ids.label_falsche.text = f"Falsche: {self.counter_F}"
                self.ids.willkommen_label.color = [1, 0, 0, 1]  # Setze die Farbe auf Rot für falsche Antwort
        else:
            print("Ungültige Eingabe: Keine Zahl")
            self.ids.willkommen_label.text = "Ungültige Eingabe"
            self.ids.willkommen_label.color = [1, 0.5, 0, 1]  # Setze die Farbe auf Orange für ungültige Eingabe



class Myyapp(MDApp):
    def build(self):
        Window.size = (411,731)
        Config.set('graphics', 'dpi', '160')
        return Builder.load_file("desi.kv")
    
if __name__ == "__main__":
    Myyapp().run()
