import msvcrt
from time import time 

def pause(heure_pause):
    return not heure_pause

def alarme(heure_alarme,minute_alarme,seconde_alarme,heure,minute,seconde):
    if heure_alarme == heure and minute_alarme == minute and seconde_alarme == seconde:
        print("\nL'Dingdong'")

def horloge(heure_base, heure_alarme, pause):
    heure = heure_base[0] ; minute = heure_base[1] ; seconde = heure_base[2]
    heure_alarme = alarme[0] ; minute_alarme = alarme[1] ; seconde_alarme = alarme[2]
    dernier_temps = time()
    affichage = alarme().upper()
    
    while True:
        if msvcrt.kbhit():
            stop = msvcrt.getch().decode('utf-8')
            if stop.lower() == 's':
                heure_pause = pause(heure_pause)
                
                heure_actuelle = time()
                temps_ecoule = heure_actuelle - dernier_temps
                
                if temps_ecoule >=1:
                    seconde += 1
                    dernier_temps = heure_actuelle
                    
                    if seconde >= 60:
                        minute += seconde //60
                        seconde %=60
                        
                        if minute >= 60:
                            heure += minute // 60
                            minute %=60
                            
                            if heure >=24:
                                heure %=24
                                
                                
heure = (15,30,0)
heure_alarme = (15,31,0)
pause = False

horloge(heure, alarme, pause)                           
                            
                
            