# D:\譚\python\HW8\midterm2.csv

# 處理 Problem / SubmitionTime / StudentID

import csv, datetime

filePath = input()
people = int(input())
studentID = input().split()	# StudentID 是一個list

fh = open(filePath, "r")
csvFile = csv.DictReader(fh)

# 
dt1 = datetime.datetime(1900,1,1,0,0,0)	# 設定初始值(problem1的)
dt2 = datetime.datetime(1900,1,1,0,0,0)	# 設定初始值(problem2的)
dt3 = datetime.datetime(1900,1,1,0,0,0)	# 設定初始值(problem3的)
dt4 = datetime.datetime(1900,1,1,0,0,0)	# 設定初始值(problem4的)
no1 = "0"
no2 = "0"
no3 = "0"
no4 = "0"
pro1 = "1"
pro2 = "2"
pro3 = "3"
pro4 = "4"

for row in csvFile:
	
	for i in range(len(studentID)):
		if row["StudentID"] == studentID[i]:	# 做 其中一個學生所有資料
			
			dt = datetime.datetime.strptime(row["SubmissionTime"], "%H:%M:%S")	# 其中這個學生的提交時間，str變datetime型態
			if row["Problem"] == "1":
				if dt > dt1:
					dt1 = dt
					no1 = studentID[i]
					
			elif row["Problem"] == "2":
				if dt > dt2:
					dt2 = dt
					no2 = studentID[i]
					
			elif row["Problem"] == "3":
				if dt > dt3:
					dt3 = dt
					no3 = studentID[i]
					
			elif row["Problem"] == "4":
				if dt > dt4:
					dt4 = dt
					no4 = studentID[i]

timelist = [[dt1,no1,pro1],[dt2,no2,pro2],[dt3,no3,pro3],[dt4,no4,pro4]]
newtimelist = sorted(timelist)
					
print(newtimelist[0][2],newtimelist[0][1])
print(newtimelist[1][2],newtimelist[1][1])
print(newtimelist[2][2],newtimelist[2][1])
print(newtimelist[3][2],newtimelist[3][1])