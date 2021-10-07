def capital_indexes(strParam):
	result = [i for i in range(len(strParam)) if strParam[i].isupper()]
	#print(result)
	return result


# Run the Function
capital_indexes("HeLlO")

