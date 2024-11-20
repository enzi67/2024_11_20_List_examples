"""
Hozz létre egy listát számokkal: [5, 8, 12, 15, 22].
Határozd meg a lista hosszát egy ciklus segítségével 
(a len() függvény megoldásán kívül használj for ciklusos megoldást is),
és írd ki!
"""
számok = [5, 8, 12, 15, 22]
print(len(számok))

szám_index = 1
for szám in számok:
    print(f"{szám_index} {szám}")
    szám_index += 1