from kivy.core.window import Window
from kivy.config import Config
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.clock import Clock
import random
import os


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
    
    def close_btn(self, dt):                        # Methode um den Startbtn sichtbar zu machen und das eigentliche Programm zu schließen
        
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
            


class Sachaufgaben(MDScreen):
    def __init__(self, **kwargs):
        super(Sachaufgaben, self).__init__(**kwargs)
    def start_sachaufgaben(self):                               ############ Zeitverzögerung für die Animation
        Clock.schedule_once(self.start_on_sachaufgaben, 0.1)    # um 0.1 Sekunden verzögern
    def start_on_sachaufgaben(self, dt):                        ############ Wird nach drücken des Start Buttons ausgelöst
        self.ids.start_btn_sachaufgaben.opacity = 0             # Start Button unsichtbar nach klick auf start
        self.ids.start_btn_sachaufgaben.disabled = True         # Start Button deaktivieren nach klick auf start
        self.ids.topcard.opacity = 1                            # MDCards sichtbar machen nach klick auf start
        self.ids.topcard.disabled = False                       # MDCards aktivieren nach klick auf start
        self.ids.middle_left_card.opacity = 1                   # MDCards sichtbar machen nach klick auf start
        self.ids.middle_left_card.disabled = False              # MDCards aktivieren nach klick auf start
        self.ids.middle_right_card.opacity = 1                  # MDCards sichtbar machen nach klick auf start
        self.ids.middle_right_card.disabled = False             # MDCards aktivieren nach klick auf start
        self.ids.bottom_left_card.opacity = 1                   # MDCards sichtbar machen nach klick auf start
        self.ids.bottom_left_card.disabled = False              # MDCards aktivieren nach klick auf start
        self.ids.bottom_middle_card.opacity = 1                 # MDCards sichtbar machen nach klick auf start
        self.ids.bottom_middle_card.disabled = False            # MDCards aktivieren nach klick auf start
        self.ids.bottom_right_card.opacity = 1                  # MDCards sichtbar machen nach klick auf start
        self.ids.bottom_right_card.disabled = False             # MDCards aktivieren nach klick auf start
        self.ids.check_answer_sachaufgaben.opacity = 1          # Beantworten Button auf Sichtbar
        self.ids.check_answer_sachaufgaben.disabled = False     # Beantworten Button auf Aktiv
        self.aufgabe_bauen_nur_bottom()

    def close_sachaufgaben(self):                               ############ Zeitverzögerung für die Animation
        Clock.schedule_once(self.close_on_sachaufgaben, 0.1)    # um 0.1 Sekunden verzögern
    def close_on_sachaufgaben(self,dt):                         ############ Wird beim drücken des Close Buttons getriggert
        self.ids.start_btn_sachaufgaben.opacity = 1             # Bei Close den Start Button wieder sichtbar machen
        self.ids.start_btn_sachaufgaben.disabled = False        # Bei Close den Start Button wieder aktivieren machen
        self.ids.topcard.opacity = 0                            # MDCards unsichtbar machen nach klick auf close
        self.ids.topcard.disabled = True                        # MDCards deaktivieren nach klick auf close
        self.ids.middle_left_card.opacity = 0                   # MDCards unsichtbar machen nach klick auf close
        self.ids.middle_left_card.disabled = True               # MDCards deaktivieren nach klick auf close
        self.ids.middle_right_card.opacity = 0                  # MDCards unsichtbar machen nach klick auf close
        self.ids.middle_right_card.disabled = True              # MDCards deaktivieren nach klick auf close
        self.ids.bottom_left_card.opacity = 0                   # MDCards unsichtbar machen nach klick auf close
        self.ids.bottom_left_card.disabled = True               # MDCards deaktivieren nach klick auf close
        self.ids.bottom_middle_card.opacity = 0                 # MDCards unsichtbar machen nach klick auf close
        self.ids.bottom_middle_card.disabled = True             # MDCards deaktivieren nach klick auf close
        self.ids.bottom_right_card.opacity = 0                  # MDCards unsichtbar machen nach klick auf close
        self.ids.bottom_right_card.disabled = True              # MDCards deaktivieren nach klick auf close
        self.ids.input_bottom_left.text = ""                    # Input auf 0 zurücksetzen
        self.ids.input_bottom_middle.text = ""                  # Input auf 0 zurücksetzen
        self.ids.input_bottom_right.text = ""                   # Input auf 0 zurücksetzen
        self.ids.input_middle_right.text = ""                   # Input auf 0 zurücksetzen
        self.ids.input_middle_left.text = ""                    # Input auf 0 zurücksetzen
        self.ids.input_top.text = ""                            # Input auf 0 zurücksetzen
        self.ids.check_answer_sachaufgaben.opacity = 0          # Beantworten Button auf Sichtbar
        self.ids.check_answer_sachaufgaben.disabled = True      # Beantworten Button auf Aktiv

    def aufgabe_bauen_nur_bottom(self):                         ############ Bauen der Methode um die Cards und Inputs mit rechnungen zu füllen
        try:
            self.num1 = random.randint(0,20)                    # Zufallszahl zwischen 0 und 20 generieren
            self.num2 = random.randint(0,30)                    # Zufallszahl zwischen 0 und 20 generieren
            self.num3 = random.randint(0,50)                    # Zufallszahl zwischen 0 und 20 generieren
            self.ids.input_bottom_left.text = str(self.num1)    # Num1 dem unteren linken input zuweisen
            self.ids.input_bottom_left.readonly = True          # Das die Zahl nicht bearbeitet werden kann
            self.ids.input_bottom_middle.text = str(self.num2)  # Num2 dem unteren mittleren input zuweisen
            self.ids.input_bottom_middle.readonly = True        # Das die Zahl nicht bearbeitet werden kann
            self.ids.input_bottom_right.text = str(self.num3)   # Num3 dem unteren rechten input zuweisen
            self.ids.input_bottom_right.readonly = True         # Das die Zahl nicht bearbeitet werden kann
        except ValueError:
            print("ERROR aufgabe_bauen")

    def check_answer_sachaufgabe(self):                             ############ Methode zum Überprüfen ob die Eingaben richtig sind
        try:
            eingabe_mitte_links = self.ids.input_middle_left.text   # Die Eingabe Mitte Links holen
            eingabe_mitte_rechts = self.ids.input_middle_right.text # Die Eingabe Mitte Rechts holen
            eingabe_top = self.ids.input_top.text                   # Die Eingabe oben holen
            eingabe_mitte_links = int(eingabe_mitte_links)          # In eine Ganzzahl umwandeln
            eingabe_mitte_rechts = int(eingabe_mitte_rechts)        # In eine Ganzzahl umwandeln
            eingabe_top = int(eingabe_top)                          # In eine Ganzzahl umwandeln
            self.num4 = self.num1 + self.num2                       # Die vierte Nummer ist Num1 + Num2
            self.num5 = self.num2 + self.num3                       # Die fünfte Nummer ist Num2 + Num3
            self.num6 = self.num4 + self.num5                       # Die sechste Nummer ist Num4 + Num5
            if eingabe_mitte_links == self.num4 and eingabe_mitte_rechts == self.num5 and eingabe_top == self.num6:
                print("Richtig")
                self.ergebnis_kurz_einblenden()                     # Wenn alles richtig ist wird das Zeitmodul aktiviert und eine neue aufgabe generiert
                
            else:
                print("Falsch")

        except ValueError:
            print("ERROR check_answer_sachaufgabe")

    def ergebnis_kurz_einblenden(self):                         ############ Wird aufgerufen wenn die Ergebnisse richtig eingegeben werden
        self.ergebnis_einblenden()                              # Zeigt den Text an der Random ausgesucht wird
        Clock.schedule_once(self.ergebnis_ausblenden, 1)        # Nach 1 Sekunde wird die Ergebnis ausblenden Methode aufgerufen
    def ergebnis_einblenden(self):                              ############ Generiert den Text und setzt das Label auf opacity = 1
        self.ids.ergebnis_sachaufgaeben.text = random.choice(["Super!", "Richtig!", "Weiter so!"])
        self.ids.ergebnis_sachaufgaeben.opacity = 1
    def ergebnis_ausblenden(self, dt):                          ############ Löscht die Inputs, und generiert eine neue Aufgabe
        self.ids.ergebnis_sachaufgaeben.opacity = 0
        self.ids.input_middle_left.text = ""
        self.ids.input_middle_right.text = ""
        self.ids.input_top.text = ""
        self.aufgabe_bauen_nur_bottom()

        
    
class Myyapp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        #Window.size = (411,731)
        #Config.set('graphics', 'dpi', '160')
        return Builder.load_file("desi.kv")
    
if __name__ == "__main__":
    Myyapp().run()


