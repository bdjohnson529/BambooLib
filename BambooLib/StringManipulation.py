#####
# String Manipulation Library
# Wrappers for Pandas dataframes
#####

# standardize strings to enable merges
def standardizeString(inputStr):
	return str(inputStr).title().strip()

# returns length of string
def GetStrLen(inputStr):
	if(inputStr):
		inputStr = str(inputStr)
		return len(inputStr)
	
	else:
		return 0

# adds a zero at the beginning of a string
def PrependZero(inputStr):
	inputStr = str(inputStr)
	outStr = '0' + inputStr
	
	return outStr