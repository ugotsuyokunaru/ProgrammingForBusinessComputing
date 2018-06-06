
num0 = input()
long = len(num0)
num = ["x"] * 8		# 只到千萬(小於一億)

chiness = dict()
chiness = {"9":"九","8":"八","7":"七","6":"六","5":"五","4":"四","3":"三","2":"二","1":"一","0":"零",}

counter = 8-1

# 建立num字串，固定四個位數，高位數不滿時補"x"
for i in range(long-1,-1,-1):
    num[counter] = chiness[num0[i]]
    counter = counter - 1

identify = 0 #變1的話代表已經有首位數了 (找到"非0"才會變1)

"""零 有夾在東西中間的話都要額外印 零 不然就會有 零十、零百等錯誤"""
# 千萬位數
if num[0] != "x":
	if (num[0] != "零" and num[3] != "零") or (num[0] != "零" and (num[1] != "零" or num[2] != "零" or num[3] != "零")): 
	#如果 (萬位數那欄不是"零") 或 (到萬位之前不是全"零")，這裡就不用"萬"
		print(str(num[0])+"千",end = "")
		identify = 1
	elif num[0] != "零" and num[3] == "零" and num[2] == "零" and num[1] == "零": #如果萬位數、十萬位數、百萬位數 欄都是零，這裡就要補"萬"
		print(str(num[0])+"千萬",end = "")
		identify = 1
		
	if num[0] == "零" and identify == 1 and ("零" not in num[1:]): #已有首位數，且後面有"非零"，才可印"零"
		print("零",end = "")

# 百萬位數
if num[1] != "x":
	if (num[1] != "零" and num[3] != "零") or (num[1] != "零" and (num[2] != "零" or num[3] != "零")):
	#如果 (萬位數那欄不是"零") 或 (到萬位之前不是全"零")，這裡就不用"萬"
		print(str(num[1])+"百",end = "")
		identify = 1
	elif num[1] != "零" and num[3] == "零" and num[2] == "零": #如果萬位數、十萬位數 欄都是零，這裡就要補"萬"
		print(str(num[1])+"百萬",end = "")
		identify = 1
	
	elif num[1] == "零" and identify ==1 and num[0] != "零" and ("零" not in num[2:]): #已有首位數，且前面那位數不是"零"(不連續"零")，且後面有"非零"，才可印"零"
		print("零",end = "")

# 十萬位數	
if num[2] != "x":
	if (num[2] != "零" and num[3] != "零"):
	#如果 (萬位數那欄不是"零")這裡就不用"萬"	(到萬位數之前 就只有自己(十萬)了)
		print(str(num[2])+"十",end = "")
		identify = 1
	elif num[2] != "零" and num[3] == "零": #如果萬位數那欄是零，這裡就要補"萬"
		print(str(num[2])+"十萬",end = "")
		identify = 1
		
	elif num[2] == "零" and identify ==1 and num[1] != "零" and ("零" not in num[3:]): #已有首位數，且前面那位數不是"零"(不連續"零")，且後面有"非零"，才可印"零"
		print("零",end = "")

# 萬位數
if num[3] != "x":
	if num[3] != "零":
		print(str(num[3])+"萬",end = "")
		identify = 1
	"""萬位數 不能補"零" """

"""因為高位數 到 萬位數 之後是另一個關卡，要重新看，故前面那位數就算是零，只要已有首位數，且後面有"非零"，千位數是零的話，還是可以印"""
# 千位數
if num[4] != "x":
	if num[4] != "零":
		print(str(num[4])+"千",end = "")
		identify = 1
	elif num[4] == "零" and identify ==1 and (num[5] != "零" or num[6] != "零" or num[7] != "零"): 
	# 因為高位數 到 萬位數 之後是另一個關卡，要重新看，故前面那位數就算是零，只要已有首位數，且後面有"非零"，千位數是零的話，還是可以印"""
		print("零",end = "")
# 百位數	
if num[5] != "x":
	if num[5] != "零":
		print(str(num[5])+"百",end = "")
		identify = 1
	elif num[5] == "零" and identify ==1 and num[4] != "零" and (num[6] != "零" or num[7] != "零"): #已有首位數，且前面那位數不是"零"(不連續"零")，且後面有"非零"，才可印"零"
		print("零",end = "")

# 十位數		
if num[6] != "x":
	if num[6] != "零":
		print(str(num[6])+"十",end = "")
		identify = 1
	elif num[6] == "零" and identify ==1 and num[5] != "零" and num[7] != "零": 
	
	# elif num[6] == ("零" and identify ==1 and num[5] != "零" and ("零" not in num[7:])) or ("零" and identify ==1 and (num[5] == "零" and num[4] != "零") and ("零" not in num[7:])):
	#(已有首位數，且前面那位數不是"零"(不連續"零")，且後面有"非零") 或 (已有首位數，且後面有"非零"，前面百位雖是"零" 但因千位不是"零"，規則上沒印出"零"的，要補印)  ，才可印"零"
		print("零",end = "")

# 個位數		
if num[7] != "x":
	if num[7] != "零":
		print(str(num[7])) #最後個位數了，不需要多印東西 或end = ""，也不可以再印"零"了
	if num[7] == "零" and identify ==0: # 如果到個位數都沒東西，個位數也是0的話，另外處理 直接印出"零"
		print("零")
		

