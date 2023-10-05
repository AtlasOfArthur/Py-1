  # Variable scope >>> Muuttuja näkyvyys (local / global || paikallinen / julkinen)

dName = "Arthur"
def displayName():
    dName = "ArthurOfTheAtlas" # Ko. funktion paikallinen muuttuja, koska se on luotu funktion sisällä.
    print(dName)

print(dName) # ei voi kutsua displayName sisällä olevaa muuttujaa näin, koska se ei ole globaali muuttuja (ei julkinen)
# Siksi tulostaa Arthur, joka on julkinen muuttuja
displayName() # Näin voi tulostaa displayName sisällä olevan arvon

# Jos laittaisin kommentin sisään displayName sisällä olevan dName muuttujan,   
# tulostaisi displayName() lähimmän saatavilla olevan tiedon. Tässä tapauksessa se olisi "Arthur"
  # "Python LEGB" (Local Enclosing Global Built-in)
print("------------------------------------------------------------")
print()
#-------------------------------------------------------------#
