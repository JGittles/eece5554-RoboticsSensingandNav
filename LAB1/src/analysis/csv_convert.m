


static = rosbag('static-updated.bag');
dynamic = rosbag('dynamic-updated.bag');


rosbag info static-updated.bag;

gps_static = select(static,'Topic', '/gps_data');
gps_dynamic = select(dynamic,'Topic', '/gps_data');

msg_static = readMessages(gps_static, 'DataFormat', 'struct')
msg_dynamic = readMessages(gps_dynamic, 'DataFormat', 'struct')

lat_s = cellfun(@(m) double(m.Latitude),msg_static);
lon_s = cellfun(@(m) double(m.Longitude),msg_static);


lat_d = cellfun(@(m) double(m.Latitude),msg_dynamic);
lon_d = cellfun(@(m) double(m.Longitude),msg_dynamic);

traj_d = [lat_d, lon_d];
writematrix(traj_d,'traj_d.csv') 

traj_s = [lat_s, lon_s];
writematrix(traj_s,'traj_s.csv') 