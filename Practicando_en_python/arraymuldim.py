lat = 34.5
lon = 45.6
posicion = [lat, lon]
historial = [[34.5, 45.6, "2022/02/02 17:20:24"], [34.5, 46.3, "2022/02/02 17:20:34"], [35.5, 47.3, "2022/02/02 17:20:441"],
[35.5, 47.3, "2022/02/02 17:20:54-1"], [34.5, 48.3, "2022/02/02 17:21:041"], [33.5, 49.3, "2022/82/82 17:21:14"]]
print(historial[0][1])
indiceLongitud = 0
indiceFLatitud = 1
indiceFecha = 2
historial_coor =[]

for poscion in historial:
    d2 = [posicion[0], poscion[1]]
    historial_coor .append(d2)

print(historial_coor)