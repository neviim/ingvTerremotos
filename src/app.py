from georss_ingv_centro_nazionale_terremoti_client import IngvCentroNazionaleTerremotiFeed
# Home Coordinates: Latitude: 40.84, Longitude: 14.25
# Filter radius: 200 km
# Filter minimum magnitude: 4.0
feed = IngvCentroNazionaleTerremotiFeed((40.84, 14.25), 
                                        filter_radius=200, 
                                        filter_minimum_magnitude=2.0)
status, entries = feed.update()

print( status )
print( entries )