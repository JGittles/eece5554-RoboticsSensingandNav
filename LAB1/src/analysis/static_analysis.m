static = rosbag('static-updated.bag');

rosbag info static-updated.bag;

gps = select(static,'Topic', '/gps_data');

msg = readMessages(gps, 'DataFormat', 'struct');

easting = cellfun(@(m) double(m.UtmEasting),msg);
northing = cellfun(@(m) double(m.UtmNorthing),msg);
altitude = cellfun(@(m) double(m.Altitude),msg);
seq = cellfun(@(m) double(m.Header.Seq),msg);
Zone = 19;
Letter = 'T';


figure(1);
scatter(easting,northing, 'b');
hold
scatter(325346.29,4693754.19,'g')

figure(2);
scatter(easting-325346.29,(northing-4693754.19)*10, 'b');

figure(3);
scatter(seq, altitude, 'r')
hold
scatter(seq, 8*ones(630,1), 'b')





