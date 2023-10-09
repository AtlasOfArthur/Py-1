  # random
import random
print("-------------")
y = random.random() # palauttaa satunnaisen liukuluvun väliltä 0 ja 1
print("y =",y)
print("-------------")
x = random.randint(1, 6)  # generoi satunnaisen kokonaisluvun 1 ja 6 välillä
print("x =",x)
print("-------------")
z = random.uniform(6.1,0.9) # palauttaa satunnaisen luikuluvun välillä 6.1 ja 9.9 
print("z =",z)
print("-------------")
print()
rpsList = ["Rock","Paper","Cissors"]
r_c = random.choice(rpsList) # Palautta satunnaisen tavaran listalta
print(r_c)
print()
print("-------------")
print()
kortit = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(kortit) # Sekoittaa kortit listan järjestyksen
print(kortit)
print()
print("-------------")
print()
# random.sample(kanta, k) on Pythonin random-moduulin funktio,
# joka palauttaa satunnaisesti valitut ainutlaatuiset elementit annetusta kannasta (kanta).
# Tässä k määrittää, kuinka monta ainutlaatuista elementtiä haluat valita.
  # Esimerkki
kortit = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
käsi = random.sample(kortit, 5)
print("Kädessäsi on kortit:",käsi) #Tulostaa korteista vain 5
print()