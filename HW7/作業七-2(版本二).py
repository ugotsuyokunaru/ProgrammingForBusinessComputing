
num0 = input()
long = len(num0)
num = ["x"] * 4		# 只到千(小於一萬)				

chiness = dict()
chiness = {"9":"九","8":"八","7":"七","6":"六","5":"五","4":"四","3":"三","2":"二","1":"一","0":"零",}

counter = 4-1

# 建立num字串，固定四個位數，高位數不滿時補"x"
for i in range(long-1,-1,-1):
    num[counter] = chiness[num0[i]]
    counter = counter - 1

"""零 有夾在東西中間的話都要額外印 零 不然就會有 零十、零百等錯誤"""
identify = 0 #變1的話代表已經有首位數了
if num[0] != "x":
	if num[0] != "零":
		print(str(num[0])+"千",end = "")
		identify = 1
	if num[0] == "零" and identify == 1 and (num[1] != "零" or num[2] != "零" or num[3] != "零"): #已有首位數，且後面有"非零"，才可印"零"
		print("零",end = "")
		
if num[1] != "x":
	if num[1] != "零":
		print(str(num[1])+"百",end = "")
		identify = 1
	elif num[1] == "零" and identify ==1 and num[0] != "零" and (num[2] != "零" or num[3] != "零"): #已有首位數，且前面那位數不是"零"(不連續"零")，且後面有"非零"，才可印"零"
		print("零",end = "")
		
if num[2] != "x":
	if num[2] != "零":
		print(str(num[2])+"十",end = "")
		identify = 1
	elif num[2] == "零" and identify ==1 and num[1] != "零" and num[3] != "零": #已有首位數，且前面那位數不是"零"(不連續"零")，且後面有"非零"，才可印"零"
		print("零",end = "")
		
if num[3] != "x":
	if num[3] != "零":
		print(str(num[3])) #最後個位數了，不需要多印東西 或end = ""，也不可以再印"零"了
	if num[3] == "零" and identify ==0: # 如果到個位數都沒東西，個位數也是0的話，另外處理 直接印出"零"
		print("零")

		


		

