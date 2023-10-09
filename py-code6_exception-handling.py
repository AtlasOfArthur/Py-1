  # exception handling

try: # Ympyröidään "vaarallinen" koodi try blokilla
    osoittaja = int(input("Anna jaettava numero: "))
    nimittäjä = int(input("Anna jakaja: "))
    vastaus = osoittaja / nimittäjä
    # print(vastaus)
  # Määritetään mitä tehdään jos tapahtuu virhe
except ZeroDivisionError:
    print("Et voi jakaa nollalla! Ääliö!")
except ValueError as e: # Esimerkki jos haluaa printata konsoliin myös virheilmoituksen
    print(e) # <<< +
    print("Vain numeroita kiitos!")
except Exception: 
    print("Jokin meni vikaan :o")
else: # Tulostaa tuloksen vain jos mitään virheitä ei satu
    print(vastaus)
finally: # Koodi, joka toistetaan aina jokatapauksessa.
    print("Tämä tulostuu aina!")

    # Olisi muös hyvä kietaista ohjelma while silmukkaan, että ohjelma jatkaisi kunnes käyttäjä antaa luvut jotka eivät aiheuta poikkeusta.