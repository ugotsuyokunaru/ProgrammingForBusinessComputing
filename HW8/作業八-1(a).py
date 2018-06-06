
import csv

# 取出csv檔案中的x,y經緯度數值，存成兩個list
def getPosition(fileName):
	fh = open(fileName, "r")
	csvFile = csv.DictReader(fh)	
	next(csvFile)	# 跳過標題列

	y_latitude = [] # to store y座標們
	x_longitude = []# to store x座標們
	
	for row in csvFile:
		y_latitude.append(row["latitude"])
		x_longitude.append(row["longitude"])
		
	fh.close()
	return [x_longitude,y_latitude]

import matplotlib.pyplot as py

x = getPosition("D:\譚\python\HW8\Myubike.csv")[0]
y = getPosition("D:\譚\python\HW8\Myubike.csv")[1]

py.plot(x,y,'o')
py.ylim(25.01 , 25.05)
py.xlim(121.52 , 121.57)
py.show()