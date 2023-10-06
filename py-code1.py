pii = 3.1415926536

print(pow(pii, pii)) #pii potenssiin pii
print("------------------------------------------------------------------------")
print()
#------------------------------------------------------------------------------#
  # [start:stop:step] (by index)
name = "Arthur Harjama"
fNameToArt = name[0:3]
lName = name[7:] #myös [7:14] (index 14 = viimeisen kirjaimen jälkeen)
funkyName = name[0:14:2] #Printtaa jokatoisen kirjaimen alusta loppuun (myös [0::2] ja [::2] printtaa saman)
reversedName = name[::-1]
funkyReversed_from_reversedName = reversedName[0::2]

print(fNameToArt + " " + lName)
print(funkyName)
print(reversedName)
print(funkyReversed_from_reversedName) #Oma räpellys testi. Näköjään toimii :)
print()
  # index operator []
# l-c-name = name[-1] # hakee nimen viimeisen kirjaimen (a ja tallentaa sen (l-c-name muuttujaan))
firstName = name[:5].upper() # muuttaa 5 ensimäistä kirjainta nimestä isoiksi.
lastName = name[7:].lower() # muuttaa seitsemännestä indeksistä eteenpäin loppuun asti kaikki pieniksi kirjaimiksi.
name = name.capitalize() # muuttaa kaikkien sanojen ensimäiset kirjaimet isoiksi
print(firstName)
print(lastName)
print(name)
print("------------------------------------------------------------------------")
print()

#------------------------------------------------------------------------------#
  #slice()
website = "http//https://en.wikipedia.org/wiki/Schumann_resonances"
website2 = "http//https://en.wikipedia.org"

sliceSchumann = slice(36, 44)
slicePedia = slice(17, -4)

print(website[sliceSchumann])
print(website2[slicePedia])
print("------------------------------------------------------------------------")
print()
#------------------------------------------------------------------------------#
  #Listat ja joitakin .metodeja

items = ["1", "2", "3", "4", "5"]
items.append("6") # Lisää loppuun itemin "6"
items.pop(1) # >>> Poistaa "2" osoittamalla sen indeksiä
# !Huom! items.pop() >>> Poistaisi (viimeisen) itemin "5" (jos 6 on lisätty, poistaisi itemin "6")
items.remove("4") # >>> Poistaa itemin "4" osoittamalla sen nimeä
print(items) # Tulostaa kaikki itemit listassa
print(items[3]) # Tulostaa itemin listasta indeksin mukaan
items.append("7")
items.insert(0, "NollaOnEka!") # Lisää indeksin 0 kohdalle itemin "NollaOnEka!"
# items.insert(2, "Kaks"), (4, "Neljä") # Ei anna erroria, mutta ei lisää itemiä "Neljä" listaan
items.insert(2, "Kaks")
items.insert (4, "Neljä")
for x in items:
    print(x) #Tulostaa yksi kerrallaan kaikki itemit listassa items käyttäen for in looppia

items.clear() # Tyhjentää koko listan
items.append("Tyhjä lista") #Lisää 'Tyhjä lista' itemin listaan
items[0] = "Ei ole tyhjä lista" # Korvaa 'Tyhjä lista' itemin
print(items) 
print("------------------------------------------------------------------------")
print()
#------------------------------------------------------------------------------#
  # 2D listat (Aka. multi dimensional lists)

juomat = ["Vesi", "Kahvi", "Mansikkamehu", "Sima", "hunajaviina", "Kalja, Piimä"]
ruoat = ["Kanapata", "Munakokkeli", "Lohi uuniperunoiden kera", "Häränpihvi kermaperunoilla", "Makaroonilaatikko, Pyttipannu"]
jälkkärit = ["Kuivakakku", "Banaanikakku", "Marjarahka", "Hedelmäjäädyke"]
# (["MUISTA", "EROTELLA LISTAN SISÄLTÖ NIIN ETTÄ", "KAIKISSA", "LISTAN JÄSENISSÄ ON", "SITAATIT"])
ravinto = [juomat,ruoat,jälkkärit]
print(ravinto) # Tulostaa ~ [[juomat lista][ruoat lista][ jälkkärit lista]]
print(ravinto[0][1]) # tulostaa Kahvi
print(ravinto[1][2]) # tulostaa Lohi uuniperunoiden kera 
print(ravinto[2][3]) # tulostaa Hedelmäjäädyke
print("------------------------------------------------------------------------")
print()
#------------------------------------------------------------------------------#
  # Tuple >>> Tietorakenne Pythonissa, joka muistuttaa listaa, mutta se on muuttumaton.

tuplebuble = () #Sen sijaan että kytettäiniin [] kuten listoissa, käytetään ()
henkilötiedotTuple = ("Amias",-1,"male")
print(henkilötiedotTuple.count("Amias")) # tulostaa 1, koska esiintyy yhden kerran
print(henkilötiedotTuple.index(-1)) # tulostaa 1, koska 8 on indeksin 1 kohdalla (0,1,2)
# Yritetään muuttaa arvo -1 toiseksi >>> (8)
# henkilötiedotTuple[1] = 8 # Antaa virheen: TypeError: 'tuple' object does not support item assignment

if "Amias" in henkilötiedotTuple:
    print("Not born yet. Stay tuned!")
print(henkilötiedotTuple)
print("------------------------------------------------------------------------")
print()
#------------------------------------------------------------------------------#
  # Set{} >>> Ei ole määriteltyä järjestystä(unindeksed), ja se ei salli duplikaatteja.

aterimet = {"haarukka","lusikka","veitsi"} # Set on nopeampi kuin list
  # Voit lisätä duplikaatteja listaan, mutta vain yksi kutakin tulostuu
astiat = {"kulho","lautanen","kuppi"}
for x in aterimet:
    print(x) # Koska järjestys on määrittelemätön, lista voi tulostua eri järjestyksessä missä se on määritetty.
    # Esim: Ensimäisessä tulostuksessa tulostui järjestyksessä >>> lusikka, veitsi, haarukka

# aterimet.append("servetti") >>> .append ei toimi. Sensijaan poistamiseen toimii .remove, kuten listoissa.
# Sen sijaan käytä >>> .add
# .clear tyhjentää setin kokonaan, kuten listan.
aterimet.add("teelusikka")
print(aterimet)
aterimet.update(astiat) # Lisää astiat setin sisällön aterimet settiin
print(aterimet)
aterimet.add("servetti")
kattaus = aterimet.union(astiat) # Yhdistää aterimet ja astiat setit uuteen settiin (kattaus)
print()
print(aterimet)
print(astiat)
print(kattaus)

astiat.add("maitolasi")
print(astiat.difference(kattaus)) # tulostaa ne jotka löytyy vain toisesta listoista (astiat ja kattaus)
# Tulostaa siis 'maitolasi'
print()
print(kattaus.intersection(astiat)) # Tulostaa kaiken sisällön joka on yhteistä molemmissa seteissä
# Huomaa että sillä ei ole väliä kummin päin setit laittaa. sama tulos tulisi myös print(astiat.intersection(kattaus))
print("------------------------------------------------------------------------")
print()
#------------------------------------------------------------------------------#
  # Dictionary on tietorakenne, joka mahdollistaa avain-arvo -parien tallentamisen.
    # Jokainen arvo on liitetty ainutlaatuiseen avainarvoon.
    # Avain toimii tunnisteena arvolle.
    # Voi muuttaa lisäämällä, muokkaamalla ja poistamalla avain-arvo -pareja.

pääkaupungit = {'USA':'Washington DC',
                'Intia':'New Delhi',
                'Kiina':'Beijing',
                'Venäjä':'Moskova'}

print(pääkaupungit['Intia']) # Tulostaa 'New Delhi'
# Huom: Jos yrittäisi tulostaa jotain mitä listassa ei ole, tulee error
# Kuten: print (pääkaupungit['Ukraina']) antaisi errorin. Turvallisempaa käyttää .get metodia
print(pääkaupungit.get('Ukraina')) # Palauttaa: None, joka kertoo että kyseistä arvoa ei ole pääkaupungeissa
print()
# voi myös tulostaa vain avaimet:
print(pääkaupungit.keys())
# tai vain arvot
print(pääkaupungit.values())
print()
# tai MOLEMMAT
print(pääkaupungit.items())

# Toinen tapa olisi käyttää for looppia
for k,v in pääkaupungit.items(): # k,v viittaa sanoihin key,value. 
  # k ja v voivat olla myös mitä tahansa muutakin, koska in osassa viitataan .items, eli kaikkiin itemeihin dictionaryn sisällä
    print(k, v) # tulostaa avaimet ja niiden arvot pareina
print()

# Voit lisätä pareja seuraavasti
pääkaupungit.update({'Saksa':'Berliini'})
# Tai myös päivittää jo olemassaolevaa tietoa
pääkaupungit.update({'USA':'New York'}) # USA pääkaupunki muuttuu New Yorkiksi
print(pääkaupungit)
pääkaupungit.pop('Venäjä') # Poistaa venäjän kirjastosta (Ei maailmankartalta)
pääkaupungit.clear() # Tyhjentää koko kirjaston
pääkaupungit.update({'Venäjä':'Moskova'})
# Lisätään varmuudenvuoksi venäjä takaisin listalle, koska ovat niin herkkiä ottamaan tällaiset asiat uhkauksina ;D 
print(pääkaupungit)
print("------------------------------------------------------------------------")
print()
#------------------------------------------------------------------------------#