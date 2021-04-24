import xlwings as xw

wb = xw.Book('test_exhell.xlsx')
sheet = wb.sheets['Sheet3']

flag = []

for i in range(6,42):

	# Get the expected value in E column
	result_cell = sheet.range(i,5)
	current_result = result_cell.value
	if current_result == False:
		expect_result = True
	else:
		expect_result = False


	input_cell = sheet.range(i,1)
	for j in range(256):
		input_cell.value = int(bin(j)[2:])
		current_result = result_cell.value
		if current_result == expect_result:
			flag.append(chr(j))
			break

print('flag{'+''.join(flag)+'}')