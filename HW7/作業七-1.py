
import datetime

year = int(input())

# 	母親節 (MOTHERS_DAY): 每年五月的第二個星期日
d1 = 0
for i in range(31):
	d = datetime.datetime(year,5,i+1).strftime("%A")
	if d == "Sunday":
		d1 += 1
		if d1 == 2:
			mother = str(datetime.date(year,5,i+1))
			
# 	祖父母節 (GRANDPARENTS_DAY): 每年8月第四個星期日
d2 = 0
for i in range(31):
	d = datetime.datetime(year,8,i+1).strftime("%A")
	if d == "Sunday":
		d2 += 1
		if d2 == 4:
			grand = str(datetime.date(year,8,i+1))
		
# 	泰雅族感恩節 (ATAYALS_DAY): 每年8月最後一個星期五	
d3 = 0
for i in range(31,0,-1):
	d = datetime.datetime(year,8,i).strftime("%A")
	if d == "Friday":
		d3 += 1
		if d3 == 1:
			taiya = str(datetime.date(year,8,i))
	
#	撒奇萊雅族火神祭 (SAKIZAYAS_DAY): 每年10月第一個星期五	
d4 = 0
for i in range(31):
	d = datetime.datetime(year,10,i+1).strftime("%A")
	if d == "Friday":
		d4 += 1
		if d4 == 1:
			saki = str(datetime.date(year,10,i+1))

#	馬丁路德紀念日(MLKINGS_DAY): 每年一月的第三個星期一			
d5 = 0
for i in range(31):
	d = datetime.datetime(year,1,i+1).strftime("%A")
	if d == "Monday":
		d5 += 1
		if d5 == 3:
			martin = str(datetime.date(year,1,i+1))
			
print("MOTHERS_DAY",mother)
print("GRANDPARENTS_DAY",grand)
print("ATAYALS_DAY",taiya)
print("SAKIZAYAS_DAY",saki)
print("MLKINGS_DAY",martin)
 
