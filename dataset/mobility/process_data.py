#!/usr/bin/env python

import numpy as np
import datetime
import time
import utm
import matplotlib.pyplot as plt
import math

def main():
	f = open('3557.txt','r')
	lines = f.readlines()
	f.close()

	northing = np.array([])
	easting = np.array([])
	timestamp = np.array([])
	zone_number = np.array([])

	print(len(lines))

	index = 0	
	for i in range(len(lines)):
		fields = lines[i].split(',')
		if(fields[2]=="0.0" or fields[3]=="0.0"):
			pass
		else:
			temp_time = time.mktime(datetime.datetime.strptime(fields[1], "%Y-%m-%d %H:%M:%S").timetuple())
			val = utm.from_latlon(float(fields[3]),float(fields[2]))

			if index != 0:
				if temp_time-timestamp[index-1]>300:
					for j in range(int(temp_time-timestamp[index-1])):
						timestamp = np.append(timestamp,temp_time)
						northing = np.append(northing,val[1])
						easting = np.append(easting,val[0])
						index += 1

				seconds_elapsed = temp_time - timestamp[index-1]
				position_uncertainity = seconds_elapsed*40

				if seconds_elapsed == 0:
					# print("Repeated Time", index, val[1], northing[index-1], val[0], easting[index-1], seconds_elapsed)					
					continue
				else:
					if(math.sqrt(math.pow(math.fabs(val[0]-easting[index-1]),2)+math.pow(math.fabs(val[1]-northing[index-1]),2))) > position_uncertainity:
						# print("Outside uncertainity", index, val[1], northing[index-1], val[0], easting[index-1], seconds_elapsed)
						continue

			timestamp = np.append(timestamp,temp_time)
			northing = np.append(northing,val[1])
			easting = np.append(easting,val[0])
			
			index += 1

	timestamp = timestamp-np.min(timestamp)
	x_direction = easting-np.min(easting)
	y_direction = northing-np.min(northing)

	x_direction = np.abs(x_direction/1).astype(int)
	y_direction = np.abs(y_direction/1).astype(int)

	print(x_direction.size, y_direction.size)

	x_direction = x_direction[0:len(x_direction):500]
	y_direction = y_direction[0:len(y_direction):500]

	print(x_direction.size, y_direction.size)

	plt.scatter(x_direction,y_direction)
	plt.show()

	zone_number = y_direction*np.max(x_direction)+x_direction

	print(np.unique(zone_number).size)

	f = open("taxi_3557_1_grids.dat","w")
	for number in zone_number:
		# print(number)
		f.write(str(number)+" ")
	f.close()

	# print(zone_number[0],y_direction[0],np.max(x_direction),x_direction[0])
	plt.plot(np.arange(len(zone_number)),zone_number)
	plt.show()

if __name__ == '__main__':
	main()