  # str.format() >>> Merkkijonojen muotoilumenetelmä, joka mahdollistaa merkkijonojen dynaamisen muotoilun.
    # Se tarjoaa joustavamman tavan liittää muuttujia merkkijonoon kuin perinteinen f-string -syntaksi (esimerkiksi f"{muuttuja}")

 # Muotoilumerkit:
   # Voit sisällyttää muotoilumerkkejä merkkijonoon, jotka toimivat paikkamerkkeinä.
   # Esimerkiksi {} toimii paikkamerkkinä, ja se korvataan myöhemmin annetulla arvolla.
 # Muuttujien asettaminen:
   # Voit antaa muotoilumenetelmälle muuttujia tai arvoja, jotka korvaavat muotoilumerkit.
   # Muuttujat annetaan str.format() -metodin kautta.
 # Paikalliset indeksit ja nimet:
   # Voit käyttää paikkaindeksejä, kuten {0} (Ensimäinen indeksi) tai nimiä määrittämään, mitkä muuttujat korvaavat mitkäkin {} paikkamerkit.
     # Esim1: muotoiltu_str = "Hei, {}! Olet {} vuotta vanha.".format(nimi, ika).
     # Esim2: muotoiltu_str = "Hei, {nimi}! Olet {ika} vuotta vanha.".format(nimi=nimi, ika=ika)
     # Esim3: muotoiltu_str = "Hei, {0}! Olet {1} vuotta vanha, vai miten se nyt meni, {0}?".format(nimi, ika)

 # Test >>> from lists
animal = ["Elephant", "Cow", "Dog", "Rat"]
item = ["Galaxy", "Solarsystem", "Moon", "Car", ]

print("The {2} jumped over the {1}, and {0} sneezed. {2:30} ...was stunned!".format(animal[3],item[0],animal[2])) # OOO.. se toimiii! ^^
                   # animal[2] ja padding 10 yksikköä ^ ^^
 # Parempi tapa:
text = ("The {} jumped over the {}, and {} sneezed. {:10} ...was stunned!")
                          # Add (10) padding to right ^
    # {:<10} padding vasemmalla, {:>10} Padding oikealla, {:^10} Padding keskitettynä
print(text.format(animal[1],item[1],animal[2],animal[3]))
print()
padding = 10 # voit määrittää paddingin sijainnin käyttämällä .rjust(), .ljust(), tai .center() 
text2 = ("The {} jumped over the {}, and {} sneezed. {} ...was stunned!")
 # Paddingin määrittely print lausekkeessa
print(text2.format(animal[3], item[0], animal[0], animal[1].center(padding))+" (Keskitetty)")
print(text2.format(animal[3], item[0], animal[0], animal[1].ljust(padding))+" (Padding oikealla)")
print(text2.format(animal[3], item[0], animal[0], animal[1].rjust(padding))+" (Padding vasemmalla)")
  # Siinä joitakin tapoja käyttää .format metodia ja paddingeja
print("------------------------------------------------------------------------")
print()
#------------------------------------------------------------------------------#
