import tkinter as tk #TK Modul importieren und als tk abkürzen
from tkinter import ttk #Möglichkeit um die neueren ttk Widgets zu importieren
from tkinter import * #Import von Tkinter und all seinen funktionen - für das Layout nötig z.B. das Widget Frame
from PIL import Image, ImageTk #Import von Bilder
from datetime import datetime #Import von Timer 

#Globale Variabeln
score_left = 0
score_right = 0
counter = 0
running = False

root = tk.Tk() #Hauptfenster erzeugen
root.title("FIFA Fussball-Weltmeisterschaft Katar 2022™") #Titel
root.geometry("1750x1000") #Dimensionen des Hauptfensters Zuerst X dann Y Werte - mit der Maus immernoch veränderbar
root.minsize(width=1600, height=600) #Mindestgrösse des Hauptfensters
root.maxsize(width=2000, height=1000) #Maximalgrösse des Hauptfensters
root.config(bg="green") #Hintergrund grün -> repräsentiert den Rasen

left_frame = Frame(root, width=400, height=550, bg="white") #Definiere ein Rahmenfenster in der GUI mit breite und höhe
left_frame.grid(row=0, column=0, padx=10, pady=5) #Gitternetz, grid, jede Zelle hat eine Zeile und eine Spalte, Padx und Pady ist die jeweilige Polsterung in X und Y Richtung


tool_bar_left = Frame(left_frame, width=300, height=550, bg="white") # Einen Rahmen im Rahmen erstellen
tool_bar_left.grid(row=2, column=0, padx=10, pady=5)

Label(left_frame, text="Schweiz").grid(row=1, column=0, padx=5, pady=5) # Beschriftung für den Rahmen

middle_frame = Frame(root, width=400, height=450, bg="white") #Definiere ein Rahmenfenster in der GUI mit breite und höhe
middle_frame.grid(row=0, column=2, padx=10, pady=15) #Gitternetz, grid, jede Zelle hat eine Zeile und eine Spalte, Padx und Pady ist die jeweilige Polsterung


tool_bar_middle = Frame(middle_frame, width=400, height=550, bg="white") # Einen Rahmen im Rahmen erstellen
tool_bar_middle.grid(row=2, column=0, padx=10, pady=5)

Label(middle_frame, text="vs.").grid(row=1, column=0, padx=5, pady=5) # Beschriftung für den Rahmen

right_frame = Frame(root, width=400, height=550, bg="white") #Definiere ein Rahmenfenster in der GUI mit breite und höhe
right_frame.grid(row=0, column=3, padx=10, pady=5) #Gitternetz, grid, jede Zelle hat eine Zeile und eine Spalte, Padx und Pady ist die jeweilige Polsterung


tool_bar_right = Frame(right_frame, width=300, height=550, bg="white") # Einen Rahmen im Rahmen erstellen
tool_bar_right.grid(row=2, column=0, padx=10, pady=5)

Label(right_frame, text="Brasilien").grid(row=1, column=0, padx=5, pady=5) # Beschriftung für den Rahmen


# Foul Funktion welche einen Eintrag in event_list schreibt
def foul_right(): #Definition vom Button Foul auf der rechten Seite 
    global event_list 
    global counter
    tt = datetime.fromtimestamp(counter)
                
    time = tt.strftime("%M:%S")
    event = time + " Foul von Brasilien"
    event_list.insert(0, event)

# Foul Funktion welche einen Eintrag in event_list schreibt
def foul_left(): #Definition vom Button Foul auf der linken Seite
    global event_list
    global counter
    tt = datetime.fromtimestamp(counter)
                
    time = tt.strftime("%M:%S")
    event = time + " Foul von der Schweiz!"
    event_list.insert(0, event)

# Rote Karte Funktion welche einen Eintrag in event_list schreibt
def rote_karte_right(): #Definition vom Button Rote Karte auf der rechten Seite
    global event_list
    global counter
    tt = datetime.fromtimestamp(counter)
                
    time = tt.strftime("%M:%S")
    event = time + " Rote Karte für Brasilien!"
    event_list.insert(0, event)

# Rote Karte Funktion welche einen Eintrag in event_list schreibt
def rote_karte_left(): #Definition vom Button Foul auf der linken Seite
    global event_list
    global counter
    tt = datetime.fromtimestamp(counter)
                
    time = tt.strftime("%M:%S")
    event = time + " Rote Karte für die Schweiz!"
    event_list.insert(0, event)

# Gelbe Karte Funktion welche einen Eintrag in event_list schreibt
def gelbe_karte_right(): #Definition vom Button Gelbe Karte auf der rechten Seite
    global event_list
    global counter
    tt = datetime.fromtimestamp(counter)
                
    time = tt.strftime("%M:%S")
    event = time + " Gelbe Karte für Brasilien!"
    event_list.insert(0, event)

# Gelbe Karte Funktion welche einen Eintrag in event_list schreibt
def gelbe_karte_left(): #Definition vom Button Gelbe Karte auf der linken Seite
    global event_list
    global counter
    tt = datetime.fromtimestamp(counter)
                
    time = tt.strftime("%M:%S")
    event = time + " Gelbe Karte für die Schweiz!"
    event_list.insert(0, event)

# Auswechslungs Funktion welche einen Eintrag in event_list schreibt
def auswechslung_right(): #Definition vom Button Auswechslung auf der rechten Seite
    global event_list
    global counter
    tt = datetime.fromtimestamp(counter)
                
    time = tt.strftime("%M:%S")
    event = time + " Auswechslung bei Brasilien!"
    event_list.insert(0, event)

# Auswechslungs Funktion welche einen Eintrag in event_list schreibt
def auswechslung_left(): #Definition vom Button Auswechslung auf der linken Seite
    global event_list
    global counter
    tt = datetime.fromtimestamp(counter)
                
    time = tt.strftime("%M:%S")
    event = time + " Auswechslung bei den Schweizern!"
    event_list.insert(0, event)
    
 # Verletzungs Funktion welche einen Eintrag in event_list schreibt   
def verletzung_right(): #Definition vom Button Verletzung auf der rechten Seite
    global event_list
    global counter
    tt = datetime.fromtimestamp(counter)
                
    time = tt.strftime("%M:%S")
    event = time + " Verletzung bei Brasilien!"
    event_list.insert(0, event)

 # Verletzungs Funktion welche einen Eintrag in event_list schreibt
def verletzung_left(): #Definition vom Button Verletzung auf der linken Seite
    global event_list
    global counter
    tt = datetime.fromtimestamp(counter)
                
    time = tt.strftime("%M:%S")
    event = time + " Verletzung bei den Schweizern!"
    event_list.insert(0, event)

 # Score (TOR) Funktion welche einen Eintrag in event_list schreibt
def score_team_left(label): #Definition vom Button TOR auf der linken Seite
    global score_left
    global event_list
    global counter
    score_left += 1
    tt = datetime.fromtimestamp(counter)
                
    time = tt.strftime("%M:%S")
    event = "%s Tor für die Schweiz! Neuer Punktestand: %s:%s" %(time, score_left, score_right)
    event_list.insert(0, event)
    label['text']=score_left, ":", score_right

# Score (TOR) Funktion welche einen Eintrag in event_list schreibt
def score_team_right(label): #Definition vom Button TOR auf der rechten Seite
    global score_right
    global event_list
    global counter
    score_right += 1
    tt = datetime.fromtimestamp(counter)
                
    time = tt.strftime("%M:%S")
    event = "%s Tor für die Brasilien! Neuer Punktestand: %s:%s" %(time, score_left, score_right)
    event_list.insert(0, event)
    label['text']=score_left, ":", score_right

 
#Label Score
label_score = tk.Label(middle_frame, text="0:0", fg="black", font="Verdana 30 bold", width=30)
label_score.grid(row=3, column=0, padx=5, pady=5)

# Button Goal linke Seite
btn_goal_left = tk.Button(left_frame, text="TOR SCHWEIZ!", command=lambda:score_team_left(label_score), width=30)
btn_goal_left.grid(row=3,  column=0, padx=5, pady=5)

# Button Foul linke Seite
btn_foul_left = tk.Button(left_frame, text="Foul SCHWEIZ!", command = foul_left, width=30)
btn_foul_left.grid(row=4,  column=0, padx=5, pady=5)

# Button rote Karte linke Seite
btn_red_card_left = tk.Button(left_frame, text="Rote Karte SCHWEIZ!", command = rote_karte_left, width=30)
btn_red_card_left.grid(row=5,  column=0, padx=5, pady=5)

# Button gelbe Karte linke Seite
btn_yellow_card_left = tk.Button(left_frame, text="Gelbe Karte SCHWEIZ!", command = gelbe_karte_left, width=30)
btn_yellow_card_left.grid(row=6,  column=0, padx=5, pady=5)

# Button Auswechslung linke Seite
btn_sub_left = tk.Button(left_frame, text="Auswechslung SCHWEIZ!", command = auswechslung_left, width=30)
btn_sub_left.grid(row=7,  column=0, padx=5, pady=5)

# Button Verletzung linke Seite
btn_injury_left = tk.Button(left_frame, text="Verletzung SCHWEIZ!", command = verletzung_left, width=30)
btn_injury_left.grid(row=8,  column=0, padx=5, pady=5)


# Button Goal rechte Seite
btn_goal_right = tk.Button(right_frame, text="TOR BRASILIEN!", command=lambda:score_team_right(label_score), width=30)
btn_goal_right.grid(row=3,  column=0, padx=5, pady=5)

# Button Foul rechte Seite
btn_foul_right = tk.Button(right_frame, text="Foul BRASILIEN!", command = foul_right, width=30)
btn_foul_right.grid(row=4,  column=0, padx=5, pady=5)

# Button rote Karte rechte Seite
btn_red_card_right = tk.Button(right_frame, text="Rote Karte BRASILIEN!", command = rote_karte_right, width=30)
btn_red_card_right.grid(row=5,  column=0, padx=5, pady=5)

# Button gelbe Karte rechte Seite
btn_yellow_card_right = tk.Button(right_frame, text="Gelbe Karte BRASILIEN!", command = gelbe_karte_right, width=30)
btn_yellow_card_right.grid(row=6,  column=0, padx=5, pady=5)

# Button Auswechslung rechte Seite
btn_sub_right = tk.Button(right_frame, text="Auswechslung BRASILIEN!", command = auswechslung_right, width=30)
btn_sub_right.grid(row=7,  column=0, padx=5, pady=5)

# Button Verletzung rechte Seite
btn_injury_right = tk.Button(right_frame, text="Verletzung BRASILIEN!", command = verletzung_right, width=30)
btn_injury_right.grid(row=8,  column=0, padx=5, pady=5)



image = Image.open("WM_Logo.jpg").resize((600, 400))
photo = ImageTk.PhotoImage(image)
Label(middle_frame, image=photo).grid(row=2, column=0, padx=5, pady=5) #Das WM Logo in den mittleren Rahmen setzen, bezieht sich auf toolbar1.grid(row=2, column=0, padx=5, pady=5)

image2 = Image.open("LogoSchweiz.webp").resize((300, 150))
photo2 = ImageTk.PhotoImage(image2)
Label(left_frame, image=photo2).grid(row=2, column=0, padx=5, pady=5) #Das Schweizer Logo in den linken Rahmen setzen, bezieht sich auf toolbar.grid(row=2, column=0, padx=5, pady=5)

image3 = Image.open("LogoBrasilien.jpg").resize((300, 150))
photo3 = ImageTk.PhotoImage(image3)
Label(right_frame, image=photo3).grid(row=2, column=0, padx=5, pady=5) #Das Brasilien Logo in den rechten Rahmen setzen, bezieht sich auf toolbar2.grid(row=2, column=0, padx=5, pady=5)



# Timer
def counter_label(label):
    def count():
        if running:
            global counter
            # Um die anfängliche Verzögerung umzugehen.
            if counter==-1:            
                display="Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                
                string = tt.strftime("%M:%S")
                display=string
   
            label['text']=display   # Or label.config(text=display)
   
            # Timer alle 1 Sekunde updaten
            label.after(1000, count) 
            counter += 1
   
    # Auslösen des Starts des Zählers
    count()     
   
# Startfunktion der Stoppuhr
def Start(label):
    global running
    running=True
    counter_label(label)
    btn_start['state']='disabled'
    btn_stop['state']='normal'
    btn_reset['state']='normal'
   
# Stoppfunktion der Stoppuhr
def Stop():
    global running
    btn_start['state']='normal'
    btn_stop['state']='disabled'
    btn_reset['state']='normal'
    running = False
   
# Reset-Funktion der Stoppuhr
def Reset(label):
    global counter
    global event_list
    global score_left
    global score_right
    score_left = 0
    score_right = 0
    label_score['text']=score_left, ":", score_right
    counter=-1
    event_list.delete(0,END) # leert die Eventanzeige
    # Wenn nach dem Drücken der Stopptaste die Reset Button gedrückt wird.
    if running==False:      
        btn_reset['state']='disabled'
        label['text']='Time!'
   
    # Wenn der Reset Button gedrück wird während laufender Stoppuhr
    else:               
        label['text']='Starting...'
   


# Label für Timer
label_timer = tk.Label(middle_frame, text="timer", fg="black", font="Verdana 30 bold", width=30)
label_timer.grid(row=5, column=0, padx=5, pady=5)

# Button für Start Timer
btn_start = tk.Button(middle_frame, text='Start', width=6, command=lambda:Start(label_timer))
btn_start.grid(row=5, column=1, padx=5, pady=5)

# Button für Stop Timer
btn_stop = tk.Button(middle_frame, text='Stop',width=6,state='disabled', command=Stop)
btn_stop.grid(row=5, column=2, padx=5, pady=5)

# Button für Reset Timer
btn_reset = tk.Button(middle_frame, text='Reset',width=6, state='disabled', command=lambda:Reset(label_timer))
btn_reset.grid(row=5, column=3, padx=5, pady=5)

# Eventlist, die alle Events speichert
event_list = Listbox(middle_frame, width=60)
event_list.grid(row=6, column=0, padx=5, pady=5)

root.mainloop() #Eventloop starten

