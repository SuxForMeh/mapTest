import pandas as pd
import folium as F
longboi = pd.read_csv("LongBoi.csv")
#53.0765452103364, 8.820692530590472
map = F.Map(location=(53.08, 8.8), zoom_start=5)

for index, row in longboi.iterrows():
    F.Marker(location=(row[2], row[3]), popup='I am a marker').add_to(map)
F.Marker((55.08, 8.8), popup='Binaur').add_to(map)
F.Marker(location=(60.08, 8.8), popup= 'I am a humanmade marker').add_to(map)

F.PolyLine(locations=[(16.350000, 81.050000), (26.383333, 80.166667)], color='blue').add_to(map)
F.PolyLine(locations=[(55.08, 8.8), (60.08, 8.8)], color='blue').add_to(map)
map.show_in_browser()
map.save("Map.html")
input("wait for exit")