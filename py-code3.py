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
  # *args >>> mahdollistaa argumenttien määrän muuttumisen funktion sisällä
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
    # Muunto listaksi yllä. ((( MUUNTAMINEN NÄIN VOI OLLA HYÖDYLLISTÄ JOS... ))) Haluaa esim. varmistaa että jotkin tietyt arvot pysyvät samoina siitä huolimatta mitä arvoja kutsun yhteydessä annetaan.
    for idx in jutskia:
        summa += idx
    return summa

print(addnums2(2,4,3,11)) # Tulostaa 20 >>> argumenttejä voi lisätä niin paljon kuin mielii
print("------------------------------------------------------------")
print() 

  # Test >>>

def randomTest(*argsTest, randomNum=15):
    uusiluku = 0
    for idx in argsTest:
        uusiluku += idx
    return uusiluku + randomNum

print(randomTest(10, 20, 30)) # Antaisi 60, mutta kun 15 on lisätty automaattisesti, antaa 75

# Ylhäällä mainitsin, että listaksi muuntaminen voi olla kätevää jos ei halua, että jotkin numerot muuttuvat.
# Jos sen sijaan haluaa, että ohjelma lisää automaattisesti tiettyjä lukuja, luulisin, että tämä on varmaan yksinkertaisin tapa.

print("------------------------------------------------------------")
print()
#-------------------------------------------------------------#
  # **kwargs ~key value arguments >>> pakkaa parametrit hakemistoon (dictionary), --- toisin kun *args, joka pakkaa parametrit tupleen
# Miksi **kwargs on hyödyllinen

  # esim:
#def hey((1,2)):
#    print("Hey "+ 1 + " " + 2)

#hey(1="First and ", 2="second", "lastly 3") # SyntaxError: invalid syntax >>> Koska funktio hyväksyy vain 2 parametria, mutta 3 yritetään antaa

  # **kwargs seim:
def heyy(**kwargs):
    for k,v in kwargs.items(): # Jos näin >>> for v in kwargs.items(): Tulostaisi: ('a', 'Moi,') ('b', 'mitä jäbä') ('c', 'duunaa') ('d', '...') ('e', 'Ai. Koodia!')
        print(v,end=" ") # end=" " >>> lisää annetut arvot peräkkäin ja takaa välilyönnit välrihin. Ilman tätä tulostaisi allekkain.

heyy(a= "Moi,",b="mitä jäbä",c="duunaa",d="...",e="Ai. Koodia!")

#- - - - - - - - - - - - - - - - - - - - - - - - - -#

  # Chat-GPT3.5 kanssa veristen kyynelien kanssa tehty esimerkki, jonka luontiin meni kaltaiseltani amatööriltä jopa tunti, vaikka tekoäly oli kaverina :'(
def kysy_arvot(**kagi):
    while True: # Eli, ajatus on siis kysyä arvoja käyttäjältä, kunnes käyttäjä antaa tyhjän
        avain = f"avain_{len(kagi) + 1}"  # Generoi avaimen automaattisesti.. BUENO!
        val = input(f"Anna arvo avaimelle '{avain}' (tyhjä lopettaa): ") # Olisi nätimpää, jos ohje olisi vain alussa, mutta menkööt nytten näin...
        # Tallentaa avaimen pariksi käyttäjän antaman arvon (val)
        if not val: # Lopeta loop, jos käyttäjä antaa tyhjän arvon (val)
            break 

        kagi[avain] = val # lisää avain-arvo -parin sanakirjaan(kagi), joka on välitetty **kagi-syntaksin kautta funktion argumenttina

    return kagi # palauttaa kagin, eli käyttäjän antamat avain-arvo parit

tulokset = kysy_arvot() # tallentaa avain-arvo parit tulokset funktioon
for key, val in tulokset.items(): # Käy läpi avain-arvo parit for in loopilla
    print(f"{val}", end=" ") # tulostaa vain arvot(val) koska emme halua niitä pareina, vaan lukukelpoisina sanojen yhdistelminä.

print("------------------------------------------------------------")
print()
#-------------------------------------------------------------#