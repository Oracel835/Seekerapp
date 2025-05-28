import serial
import pandas as pd
from datetime import datetime

# Verbindung mit dem loRa-device öffenen (COM-Port je nach Gerät anpassen)
ser = serial.Serial('COM', 9600, timeout= 1)

#Optional datei zum Mitspeichern
csv_file = "signal_data.csv"
df = pd.DataFrame(columns=["timestamp", "rssi", "snr", "gps_lat", "gps_lon"])

try:
    while True:
        raw = ser.readline().decode().strip()
        if raw:
            print(f"Emfang:{raw}")
            # Beispiel-Datenformat: "RSSI:-70,SNR:7,GPS:52.52,13.40"
            parts = raw.split(",")
            data = {
                "timestamp":datetime.now().isoformat(),
                "rssi": int(parts[0].split(":")[1]),
                "snr": float(parts[1].split(":")[1]),
                "gps_lat": float(parts[2].split(":")[1]),
                "gps_lon": float(parts[3])    
            }
            df = pd.concat([df,pd.DataFrame([data])], ignore_index=True)
            df.to_csv(csv_file, index=False)
except KeyboardInterrupt:
    print("Abruch durch tastatur.")
    ser.close()
