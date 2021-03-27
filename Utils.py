def integerToBinaryString(integer):
	return bin(integer).replace("0b", "")

def stringToBoolean(string, trueValues = ["yes", "1", "t", "true"]):
	return string in trueValues