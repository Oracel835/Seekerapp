from mapping_Visualisation_folium import create_folium_map
from mapping_Visualisation_heatmap_plot import create_heatmap
import webbrowser
#Software Startpunkt
if __name__ == "__main__":
    print("Commence seeker-Spftware...")
    
    # Debug-Ausgaben hinzufügen
    print("Erstelle Folium Map...")
    create_folium_map()

    print("Öffne HTML-Datei im Browser...")
    webbrowser.open("signal_map.html")

    print("Erstelle Heatmap...")
    create_heatmap()

    webbrowser.open("signal_map.html")