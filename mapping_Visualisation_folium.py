import folium
import folium.map
import pandas as pd
from folium.plugins import HeatMap

def create_folium_map():
    print("Karte wird erstellt")

# 1.CSV-datei mit Messdaten laden
df = pd.read_csv("signal_data.csv")

# 2.Map-Zentrum (z.B. Mittelpunkt der position)
center_lat = df["gps_lat"].mean()
center_lon = df["gps_lon"].mean()

# 3. Erstelle eine karte mit Zentrum
m = folium.Map(location = [center_lat, center_lon], zoom_start = 15)

# 4.Marker mit RSSI pop-up
for _, row in  df.iterrows():
    if row["rssi"] > -75:
        folium.Marker(
        location=[row["gps_lat"], row["gps_lon"]],
        popup = f"RSSI: {row['rssi']} dBm\nSR: {row['snr']}"
        ).add_to(m)
    
# 5.Heatmap (optional: normalize rssi 0-1)
heat_data = [
    [ row["gps_lat"], row["gps_lon"], row["rssi"]] for _, row in df.iterrows()
]
HeatMap(heat_data, radius=15).add_to(m)

# 6.HTML speichern
m.save("signal_map.html")
print(":D Karte speichernals 'signal_map.html'. Öffenen sie im Browser")