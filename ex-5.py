def time24hr(tstr):
	if "am" in tstr:
		morning = tstr.strip("am").split(":")
		if morning[0] == '12':
			hours = '00'+ morning[1]+'hr'
		elif int(morning[0])<10:
			hours = '0' + morning[0]+morning[1]+'hr'
		else:
			hours = morning[0] + morning[1] + 'hr'

		return hours

	else:
		afternoon = tstr.strip("pm").split(":")
		if afternoon[0] == '12':
			hours = afternoon[0] + afternoon[1] + 'hr'
		else:
			hours = str(12+int(afternoon[0]))+afternoon[1] +'hr'

		return hours

print time24hr("3:20am")
print time24hr("11:20am")
print time24hr("12:34am")
print time24hr("5:26pm")