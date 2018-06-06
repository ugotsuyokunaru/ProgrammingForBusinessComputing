
num0 = input()
long = len(num0)
num = [0] * long

for i in range(long):
	if num0[i] == "9":
		num[i] = "九"
	if num0[i] == "8":
		num[i] = "八"
	if num0[i] == "7":
		num[i] = "七"
	if num0[i] == "6":
		num[i] = "六"
	if num0[i] == "5":
		num[i] = "五"
	if num0[i] == "4":
		num[i] = "四"
	if num0[i] == "3":
		num[i] = "三"
	if num0[i] == "2":
		num[i] = "二"
	if num0[i] == "1":
		num[i] = "一"
	if num0[i] == "0":
		num[i] = "零"

#千位數
if long == 4:
	"""零 有夾在東西中間的話都要額外印 零 不然就會有 零十、零百等錯誤"""
	## X000
	if num[0] != "零" and num[1] == "零" and num[2] == "零" and num[3] == "零":
		print(str(num[0])+"千")
		
	## XX00
	elif num[0] != "零" and num[1] != "零" and num[2] == "零" and num[3] == "零":
		print(str(num[0])+"千"+str(num[1])+"百")
	## X00X
	elif num[0] != "零" and num[1] == "零" and num[2] == "零" and num[3] != "零":
		print(str(num[0])+"千"+"零"+str(num[3]))
	## X0X0
	elif num[0] != "零" and num[1] == "零" and num[2] != "零" and num[3] == "零":
		print(str(num[0])+"千"+"零"+str(num[2])+"十")

	## XXX0
	elif num[0] != "零" and num[1] != "零" and num[2] != "零" and num[3] == "零":
		print(str(num[0])+"千"+str(num[1])+"百"+str(num[2])+"十")
	## XX0X
	elif num[0] != "零" and num[1] != "零" and num[2] == "零" and num[3] != "零":
		print(str(num[0])+"千"+str(num[1])+"百"+"零"+str(num[3]))
	## X0XX	
	elif num[0] != "零" and num[1] == "零" and num[2] != "零" and num[3] != "零":
		print(str(num[0])+"千"+"零"+str(num[2])+"十"+str(num[3]))
		
	## 沒有0		
	elif num[0] != "零" and num[1] != "零" and num[2] != "零" and num[3] != "零":
		print(str(num[0])+"千"+str(num[1])+"百"+str(num[2])+"十"+str(num[3]))

#百位數
elif long == 3:
	# x00
	if num[0] != "零" and num[1] == "零" and num[2] == "零":
		print(str(num[0])+"百")
	# x0x
	elif num[0] != "零" and num[1] == "零" and num[2] != "零":
		print(str(num[0])+"百"+"零"+str(num[2]))
	# xx0
	elif num[0] != "零" and num[1] != "零" and num[2] == "零":
		print(str(num[0])+"百"+str(num[1])+"十")
	# 沒有0
	elif num[0] != "零" and num[1] != "零" and num[2] != "零":
		print(str(num[0])+"百"+str(num[1])+"十"+str(num[2]))

#十位數
elif long == 2:
	# x0
	if num[0] != "零" and num[1] == "零":
		print(str(num[0])+"十")
	# 沒有0
	elif num[0] != "零" and num[1] != "零":
		print(str(num[0])+"十"+str(num[1]))

#個位數
elif long == 1:	
	print(str(num[0]))
