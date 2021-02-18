import folium
import csv


dynamic = []
target = [(42.37654, -71.12189), (42.37649, -71.11989)]

with open('traj_d.csv',newline='') as csvfile:
    reader=csv.reader(csvfile, delimiter=' ')
    for row in reader:
        temp =[]
        row = row[0].split(',')
        temp.append(float(row[0]))
        temp.append(float(row[1]))


        dynamic.append(temp)



m = folium.Map(location=[42.37, -71.12], zoom_start=15)
folium.TileLayer('open street map').add_to(m)
folium.PolyLine(dynamic, color="red").add_to(m)
folium.PolyLine(target, color="blue").add_to(m)




m.save('dynamic_map.html')