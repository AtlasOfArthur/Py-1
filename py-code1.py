pii = 3.1415926536

print(pow(pii, pii)) #pii potenssiin pii

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

#------------------------------------------------------------------------------#
  #slice()
website = "http//https://en.wikipedia.org/wiki/Schumann_resonances"
website2 = "http//https://en.wikipedia.org"

sliceSchumann = slice(36, 44)
slicePedia = slice(17, -4)

print(website[sliceSchumann])
print(website2[slicePedia])

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

