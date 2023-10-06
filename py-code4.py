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

