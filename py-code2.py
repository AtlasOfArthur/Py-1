  # funktiot >>> pala koodia, joka ajetaan vain kun sitä kutsutaan
    # return

def definitionEliFunktio():
    print() # Tyhjä rivi
    print("En toista samaa koodia...")
    print("Tämä säästää tilaa ja muistia!")
    print() # Tyhjä rivi

def moi(nimi):
    print("No moi "+nimi+"!")

# HUOM. Koodit eivät sisällä 'return' lauseketta. siksi konsolissa lukee None kun funktiota yritetään printata
definitionEliFunktio()
print(moi("Arthur")) # normaalisti kutsuttaisiin näin: moi("Arthur")
# Printtaa konsoliin: None
moi("Arthurius") # näin
definitionEliFunktio()

def old(ikä=36): # Annetaan parametrille ikä heti arvo 36 (int)
    return (ikä)

def enimi():
    etunimi = "Arthur"
    return etunimi # Kun funktion arvo palautetaan, sitä voidaan käyttää muualla

def lisääSukunimi(onKokonimi):
    print("Hei "+ enimi() +" "+onKokonimi) # Lisätään viesti, sitten erillisellä funktiolla ennalta määritetyn etunimi ja lopuksi jonka arvo määritetään myöhemmin
    print("Hyvää päivänjatkoa!")

lisääSukunimi("Harjama"+" "+str(old())) # Lisätään funktiossa olevaan parametriin sukunimi ja saadaan aikaan viesti jonka sukunimi osa on modifioitavissa parametrin kautta
# Lisätty myös ikä funktiosta old() ja muunnettu se stringiksi, jotta tulostaa numeron 36

def ikäUpdate(updateOld):
    updateOldResult = old() + updateOld
    return updateOldResult # Vpisi myös palauttaa suoreen edellisellä rivillä >>> return old() + updateOld

uP = ikäUpdate(1)
print(uP) # Tulostaa 37 
# Toinen tapa >>> print(ikäUpdate(1))

print("------------------------------------------------------------")
print()
#-------------------------------------------------------------#
  # Avainsana argumentit

def avainsanat(eka,toka,vika):
    print("moi "+eka+toka+vika)

avainsanat("Arthur","Atlas","Of") # Printtaa annetussa järjestyksessä
avainsanat(vika="Arthur",eka="Atlas",toka="Of") #Printtaa oikeassa järjestyksessä kun viitataan avainsanoilla (eka,toka,vika)

print("------------------------------------------------------------")
print()
#-------------------------------------------------------------#
  #Sisäkkäinen funktiokutsu ~~'Ketjutettu funktiokutsu'
  
#Tapa1
num = input("Anna positinen numero: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)

#Tapa2, Esimerkki1
print(round(abs(float(input("Anna positiivinen numero: ")))))

# Esimerkki2
def neliojuuri(x):
    return x ** 0.5

def kahdella_korotettu(x):
    return x ** 2

def tuplattu(x):
    return x * 2

def vahennetty_kolmella(x):
    return x - 3

alkuluku = float(input("Syötä luku: "))

tulos = vahennetty_kolmella(tuplattu(kahdella_korotettu(neliojuuri(alkuluku))))

print("Tulos:", tulos)
