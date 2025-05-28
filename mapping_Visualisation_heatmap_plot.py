import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_heatmap():
    print("Heatmap (Matplotlib) wird erstellt.")

    # 1. csv-daten laden
    df = pd.read_csv("signal_data.csv")

    # 2.GPS-Koordinaten laden
    lats = df["gps_lat"].values 
    lons = df["gps_lon"].values
    rssis = df["rssi"].values

 # 3. Grid erstellen
    heatmap, xedges, yedges = np.histogram2d(
        lats, lons, bins=(100, 100), weights=rssis
    )

    extent = [yedges[0], yedges[-1], xedges[0], xedges[-1]]


    # Streudiagramm als Heatmap
    plt.imshow(
        heatmap.T,origin='lower', cmap='inferno',
        extent=extent, aspect='auto'
    )
    plt.colorbar( label='RSSI (dBm)')
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Signal Heatmap (2D)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

create_heatmap()