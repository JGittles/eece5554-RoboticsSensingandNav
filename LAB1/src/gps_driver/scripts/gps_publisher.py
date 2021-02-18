#!/usr/bin/env python

import serial
import rospy
import utm
from std_msgs.msg import String
from gps_driver.msg import Gps
port = serial.Serial("/dev/pts/8", baudrate=4800, timeout=3.0)

seq=0


def gpggaToDeg(str_val, direction):
    if direction == 'N' or direction == 'E':
        sign = 1
    else:
        sign = -1

    if direction == 'N' or direction == 'S':
        deg = int(str_val[:2])
        min = float(str_val[2:])

    else:
        deg = int(str_val[:3])
        min = float(str_val[3:])

    return sign*(deg + min/60)
    

def utcToSec(str_val):
    hour=(int(str_val[:2]))
    min=(int(str_val[2:4]))
    sec=(float(str_val[4:]))


    return (hour*3600) + (min*60) + sec








if __name__ == "__main__":
    rospy.init_node('gps_driver', anonymous=True)
    pub = rospy.Publisher('gps_data', Gps, queue_size=5)
    pub_raw = rospy.Publisher('gps_raw_data', String, queue_size=5)
    data_update = Gps()
    file = open(str(rospy.Time.now())+".txt", "w")
        
    while not rospy.is_shutdown():
        rcv = port.readline()
        try:
            if "GPGGA" in rcv:

                data_update.raw_data = rcv
                file.write(rcv+"\n")

                raw_data=rcv.split(",")

               # print(repr(raw_data))

                lat = gpggaToDeg(raw_data[2], raw_data[3])
                lon = gpggaToDeg(raw_data[4], raw_data[5])
                utm_data = utm.from_latlon(lat, lon)


                data_update.latitude = lat
                data_update.longitude = lon
                data_update.altitude = float(raw_data[9])
                data_update.utm_easting = utm_data[0]
                data_update.utm_northing = utm_data[1]
                data_update.zone = utm_data[2]
                data_update.letter = utm_data[3]

                data_update.header.stamp.secs = utcToSec(raw_data[1])
                data_update.header.stamp.nsecs = 0
                data_update.header.frame_id = raw_data[0]
                data_update.header.seq = seq
                

                rospy.loginfo(raw_data)
                rospy.loginfo(data_update)

                pub.publish(data_update)
                pub_raw.publish(rcv)


                seq = seq + 1

                rospy.sleep(1/4800)

       # except Exception as e:
        #    print(e)

        except rospy.ROSInterruptException: 
            file.close()
            port.close()



