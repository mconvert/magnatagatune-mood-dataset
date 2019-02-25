if __name__ == "__main__":
	fannotations = open("../data/annotations_final.csv", "r")
	output = open("../data/annotations.csv", "w")

	text = fannotations.read()

	string = ""
	for char in text:
		if char == "	":
			string = string + ","
		else:
			string = string + char

	output.write(string)
	fannotations.close()
	output.close()

