

dynamic = rosbag('dynamic-updated.bag');

rosbag info dynamic-updated.bag;

gps = select(dynamic,'Topic', '/gps_data');

msg = readMessages(gps, 'DataFormat', 'struct');

easting = cellfun(@(m) double(m.UtmEasting),msg);
northing = cellfun(@(m) double(m.UtmNorthing),msg);
seq = cellfun(@(m) double(m.Header.Seq),msg);
altitude = cellfun(@(m) double(m.Altitude),msg);
Zone = 19;
Letter = 'T';

easting_ref=[325306.20 325470.72]
northing_ref=[4693765.19 4693755.53]
p1=[325306.20 4693765.19 8]
p2=[325470.72 4693755.53 8]
v=[p1; p2]



figure(1);
scatter(easting,northing, 'b');
hold
plot(easting_ref,northing_ref,'g');

point=[easting,northing,altitude]
figure(2);
plot3(point(:,1),point(:,2),point(:,3))
hold
plot3(v(:,1),v(:,2),v(:,3))

figure(3);
scatter(seq, altitude, 'r')
hold
scatter(seq, 8*ones(155,1), 'b')



