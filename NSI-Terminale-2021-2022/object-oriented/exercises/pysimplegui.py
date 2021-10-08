#import PySimpleGUIWeb as sg
import PySimpleGUI as sg
from random import randint
# ---------------------------- Fonctions et classes --------------------------------------
class IndividuT1():    
    
    def __init__(self, x, y, label, couleurTexte, couleurFond):        
        self.x = x        
        self.y = y        
        self.label = label        
        self.couleurTexte = couleurTexte        
        self.couleurFond = couleurFond    
        
    def deplacerHorizontal(self):        
        if self.x <  MAX_COL - 1:            
            self.x +=1        
        else:            
            self.x = 0            
            if self.y <  MAX_ROWS - 1:                
                self.y +=1            
            else:                
                self.y = 0

    def deplacerVertical(self):
        if self.y < MAX_ROWS - 1:
            self.y += 1
        else:
            self.y = 0
            if self.x < MAX_COL -1:
                self.x += 1
            else:
                self.y = 0

# -------------- Programme principal - Appel des fonctions -------------------------------------

# ---- Initialisation ----

# -- Objets de type Individu --
individu1 = IndividuT1(0, 0,'+', 'white','purple') # (x, y, label, couleurTexte, couleurFond)
individu2 = IndividuT1(0, 0, "-", "white", 'purple')
# -- Paramètres de l'inteface graphique --
MAX_ROWS = MAX_COL = 10
board = [[randint(0,1) for j in range(MAX_COL)] for i in range(MAX_ROWS)]
layout =  [[sg.Button('?', size=(1, 1), key=(i,j), pad=(0,0)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]
window = sg.Window('Déplacer objets de type cellule', layout)

# ---- Boucle principale GUI ----
while True:    
    event, values = window.read(timeout=100)    
    if event in (sg.WIN_CLOSED, 'Exit'):        
        break    

    # window[(row, col)].update('New text')  
    # To change a button's text, use this pattern    
    # For this example, change the text of the button to the board's value and turn color black        
    i = individu1.y    
    j = individu1.x    
    label = individu1.label    
    couleurTexte = individu1.couleurTexte   
    couleurFond = individu1.couleurFond   
    window[(i, j)].update(label, button_color=(couleurTexte,couleurFond)) 

    i = individu2.y    
    j = individu2.x    
    label = individu2.label    
    couleurTexte = individu2.couleurTexte   
    couleurFond = individu2.couleurFond   
    window[(i, j)].update(label, button_color=(couleurTexte,couleurFond)) 

    individu1.deplacerVertical()
    individu2.deplacerHorizontal()
# ---- Fin / Fermer fenêtre graphique ----
window.close()