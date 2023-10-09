  # Perus tiedoston havaitseminen
import os
# path = "C:\Users\\arthur\\source\\Py1\\Py-Repo1\\test.txt"
path = "C:\\Users\\arthur\\source\\Py1\\Py-Repo1\\testFolder"

if os.path.exists(path):
    print("Sijainti on olemassa.")
    if os.path.isfile(path):
        print("Kyseessä on tiedosto.")
    elif os.path.isdir(path):
        print("Kyseessä on kansio")
else:
    print("Sijaintia ei ole olemassa.")
print()
print("-----------------------------------------")
#----------------------------------------------#
  # Tiedoston sisällön lukeminen
print()
with open('test.txt') as file: # Koska tiedosto on samassa kansiossa tämän tiedoston kanssa, ei koko polkua tarvita.
    print(file.read()) # Kyllä se sen lukee, mutta heikosti kun ei ole tukea suomenkielen kirjaimistolle
print(file.close) # palauttaa true, koska tiedosto ei ole auki. Eli tämä (with open) on sinänsä kätevää, koska ohjelma ei jätä tiedostoa auki kun se on luettu.
print()
try: # Huomaa virhe tiedostonimessä
    with open('test.tx') as file:
            print(file.read())
    print(file.close)
except FileNotFoundError:
     print("Tiedostoa ei löytynyt. tarkista mahdolliset kirjoitusvirheet.")
print()
print("-----------------------------------------")
#----------------------------------------------#
  # Tiedostojen kirjoittaminen pythonilla
text2 = "YoOoOoOoOoOoOoOooo\nThis is some text!\nYeaah! Mitähän tällä tekis?\n"
with open('test2.txt','w') as file: # r lukee tiedoston >>> w kirjoittaa siihen
    file.write(text2) # Koodi luo tiedoston itse, joten sitä ei tarvitse luoda erikseen.
    print(text2)
    # Huomaa, että jos tiedostossa oli aikaisemmin tekstiä, tämä korvaa tiedostossa olleen tekstin.
text2 = "Tämä!\n...eli\nTHIS\n REPLACES THE PREVIOUS TEXT\n"
with open('test2.txt','w') as file: 
     file.write(text2)
     print(text2) # Avaamalla tiedoston voit tarkistaa, että vain toinen teksteistä on olemassa.

# On myös mahdollista lisätä tekstiä tiedostoon, ilman että se korvautuu:
text2 = "\n. . . APPEND THIS . . .\n"
with open('test2.txt','a') as file: # a niinkuin append
     file.write(text2)
     print(text2)
     print()
print("-----------------------------------------")
#----------------------------------------------#
  # Tiedostin kopiointi >>> copyfile() kopioi tiedoston sisällön
                    #   >>> copy() = copyfile() + lupa tila + määränpää voi olla hakemisto
                    #   >>> copy2() = copy() + kopioi metadatan
import shutil 
shutil.copyfile('test2.txt','copyOftest2.txt') # source,destination
print()
print("-----------------------------------------")
#----------------------------------------------#
  # Tiedostojen siirtäminen pythonilla
# import os tehty jo ylempänä

sijainti = "moveTest.txt" # "C:\\Users\\arthur\\source\\Py1\\Py-Repo1\\moveTest.txt"
määränpää = "C:\\Users\\arthur\\source\\Py1\\\Py-Repo1\\testFolder"

try:
    if os.path.exists(määränpää):
        print("Määränpäässä on jo tiedosto.") # En tiedä miksi väittää että määränpäässä on jo tiedosto... kun ei ole.
    else:
        os.replace(sijainti,määränpää)
        print(sijainti+" siirrettiin")
except FileNotFoundError:
     print(sijainti+" ei havaittu")