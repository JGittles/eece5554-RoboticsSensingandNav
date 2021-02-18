import folium
import csv


static = []
target = (42.37645, -71.1214)

with open('traj_s.csv',newline='') as csvfile:
    reader=csv.reader(csvfile, delimiter=' ')
    for row in reader:
        temp =[]
        row = row[0].split(',')
        temp.append(float(row[0]))
        temp.append(float(row[1]))


        static.append(temp)



m = folium.Map(location=[42.37, -71.12], zoom_start=15)
folium.TileLayer('open street map').add_to(m)
for i in static:
    folium.Marker(location= i, icon=folium.Icon(color="red")).add_to(m)
folium.Marker(target, color="blue").add_to(m)




m.save('static_map.html')