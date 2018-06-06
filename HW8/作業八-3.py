
# D:\譚\python\HW8\midterm2.csv
# 10:00:00 10:20:00

import csv, datetime

filePath = input()
timeRange = input().split()
start = datetime.datetime.strptime(timeRange[0], "%H:%M:%S")		# 開始時間(型態:datetime)
end = datetime.datetime.strptime(timeRange[1], "%H:%M:%S")		# 結束時間(型態:datetime)

fh = open(filePath, "r")
csvFile = csv.DictReader(fh)

# 定義新型態ProblemInfo()，包含題目要求的五種status
class ProblemInfo:
	AC = int(0)
	CE = int(0)
	RE = int(0)
	TLE = int(0)
	WA = int(0)

# 依照csv檔中的problem1~4，開4個新變數，型態為自訂型態ProblemInfo()，可記錄5種attribute的次數
Pro1 = ProblemInfo() # to store status
Pro2 = ProblemInfo() # to store status
Pro3 = ProblemInfo() # to store status
Pro4 = ProblemInfo() # to store status

# 分別處理csv檔中的problem1~4，各自累加5種attribute的次數
for row in csvFile:
	dt = datetime.datetime.strptime(row["SubmissionTime"], "%H:%M:%S")
	# print(dt) # 記得刪掉
	
	if start <= dt <= end:	#提交時間 有在限定時間內者
		if row["Problem"] == "1":
			if row["Status"] == "Accepted":
				Pro1.AC += 1
			elif row["Status"] == "Compile Error":
				Pro1.CE += 1
			elif row["Status"] == "Runtime Error":
				Pro1.RE += 1
			elif row["Status"] == "Time Limit Exceed":
				Pro1.TLE += 1
			elif row["Status"] == "Wrong Answer":
				Pro1.WA += 1
		elif row["Problem"] == "2":
			if row["Status"] == "Accepted":
				Pro2.AC += 1
			elif row["Status"] == "Compile Error":
				Pro2.CE += 1
			elif row["Status"] == "Runtime Error":
				Pro2.RE += 1
			elif row["Status"] == "Time Limit Exceed":
				Pro2.TLE += 1
			elif row["Status"] == "Wrong Answer":
				Pro2.WA += 1
		elif row["Problem"] == "3":
			if row["Status"] == "Accepted":
				Pro3.AC += 1
			elif row["Status"] == "Compile Error":
				Pro3.CE += 1
			elif row["Status"] == "Runtime Error":
				Pro3.RE += 1
			elif row["Status"] == "Time Limit Exceed":
				Pro3.TLE += 1
			elif row["Status"] == "Wrong Answer":
				Pro3.WA += 1
		elif row["Problem"] == "4":
			if row["Status"] == "Accepted":
				Pro4.AC += 1
			elif row["Status"] == "Compile Error":
				Pro4.CE += 1
			elif row["Status"] == "Runtime Error":
				Pro4.RE += 1
			elif row["Status"] == "Time Limit Exceed":
				Pro4.TLE += 1
			elif row["Status"] == "Wrong Answer":
				Pro4.WA += 1

print(Pro1.AC , Pro1.CE , Pro1.RE , Pro1.TLE , Pro1.WA)
print(Pro2.AC , Pro2.CE , Pro2.RE , Pro2.TLE , Pro2.WA)
print(Pro3.AC , Pro3.CE , Pro3.RE , Pro3.TLE , Pro3.WA)
print(Pro4.AC , Pro4.CE , Pro4.RE , Pro4.TLE , Pro4.WA)