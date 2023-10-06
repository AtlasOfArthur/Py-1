  # Variable scope >>> Muuttuja näkyvyys (local / global || paikallinen / julkinen)

dName = "Arthur"
def displayName():
    dName = "ArthurOfTheAtlas" # Ko. funktion paikallinen muuttuja, koska se on luotu funktion sisällä.
    print(dName) # Jos olisi palautettu >>> return dName >>> voisi silloin käyttää muualla, esim: displayName(dName)

print(dName) # ei voi kutsua displayName sisällä olevaa muuttujaa näin, koska se ei ole globaali muuttuja (ei julkinen)
# Siksi tulostaa Arthur, joka on julkinen muuttuja
displayName() # Näin voi tulostaa displayName sisällä olevan arvon
#displayName(dName) # Antaa errorin, koska arvoa ei ole palautettu, jotta se olisi saatavilla. (Ks. rivi 6)

# Jos laittaisin kommentin sisään displayName sisällä olevan dName muuttujan,   
# tulostaisi displayName() lähimmän saatavilla olevan tiedon. Tässä tapauksessa se olisi "Arthur"
  # "Python LEGB" (Local Enclosing Global Built-in)
print("------------------------------------------------------------")
print()
#-------------------------------------------------------------#
  # *args >>> mahdollistaa muuttuvan määrän argumentteja funktion sisällä
    # *args pakkaa kaikki sille annetut argumentit tupleen.
    # Tämä tarkoittaa sitä, että vaikka voisit kutsua funktiota eri määrällä argumentteja, ne kaikki käsitellään yhtenä tuple-na funktion sisällä

#def addnums(num1,num2):
#    summa = num1 + num2
#    return summa

#print(addnums(2,4,3)) # Tulostaisi 9 jos ei antaisi erroria. Antaa errorin, koska funktio pystyy hyväksymään vain 2 arvoa

def addnums2(*jutskia): # Voi nimetä miksikä vain. tärkeintä on että edessä on >>> *
    summa = 0
    # jutskia[0] = 0  # >>> antaa errorin, koska tuppleja ei voi muuttaa. MUTTA! tähän on poikkeus, jos muunat tuplen listaksi.
    # Tupplen muunto listaksi alla
    jutskia = list(jutskia)
    jutskia[0] = 12 # muuttaa numeron 2, joka on indeksissä 0, numeroksi 12. tulos on siis 20 sijaan 30.
    # Muunto listaksi yllä
    for idx in jutskia:
        summa += idx
    return summa

print(addnums2(2,4,3,11)) # Tulostaa 20 >>> argumenttejä voi lisätä niin paljon kuin mielii
print("------------------------------------------------------------")
print()
#-------------------------------------------------------------#