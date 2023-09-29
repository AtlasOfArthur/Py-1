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

