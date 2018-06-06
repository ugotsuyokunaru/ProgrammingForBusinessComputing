
import csv, math

# 取出csv檔案中的x,y經緯度數值，存成兩個list
def getPosition(fileName):
		fh = open(fileName, "r")
		csvFile = csv.DictReader(fh)	
		next(csvFile)	# 跳過標題列

		y_latitude = [] # to store y座標們
		x_longitude = []# to store x座標們
	
		for row in csvFile:
			y_latitude.append(float(row["latitude"]))
			x_longitude.append(float(row["longitude"]))
		
		fh.close()
		return [x_longitude , y_latitude]
x = getPosition("D:\譚\python\HW8\Myubike.csv")[0]
y = getPosition("D:\譚\python\HW8\Myubike.csv")[1]
	
# 算距離的函數
def haversine(lat1, lon1, lat2, lon2):
	lon1, lat1, lon2, lat2 = map(math.radians , [lon1, lat1, lon2, lat2])
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = math.sin(dlat / 2) ** 2
	a += math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
	return 6367 * (2 * math.asin(math.sqrt(a)))

# 定義Station()新型態，有計算距離的member function	
class Station:
	long = float()
	lat = float()
	
	def __init__(self,long,lat):
		self.long = long
		self.lat = lat
	
	def distance(self,other):
		return haversine(self.lat , self.long , other.lat , other.long )
		
stations = []		# 每個元素都是一個Station()型態list
for i in range(len(x)):
	gg = Station(x[i] , y[i])
	stations.append(gg)
		
# 找出所有車站之間距離(包括自己到自己的距離為0)，找出距離最長的

maxDistance = 0	#初始值設為0
for i in range(len(stations)):	
	for j in range(len(stations)):
		Distance = stations[i].distance(stations[j])
		if Distance > maxDistance:
			# 紀錄最長距離
			maxDistance = Distance
			# 紀錄要存成紅點的兩組座標
			latR = stations[i].lat
			longR = stations[i].long
			latR2 = stations[j].lat
			longR2 = stations[j].long
			
import matplotlib.pyplot as py

py.plot(x,y,'bo')
py.plot(longR ,latR,'ro')
py.plot(longR2 ,latR2,'ro')
py.ylim(25.01 , 25.05)
py.xlim(121.52 , 121.57)
py.show()