import pandas as pd

def mood_count(row, tags):
	""" Auxiliary function counting the presence of mood tags in a row.
	"""
	count = 0

	for tag in tags:
		count += int(row[tag])

	return count


if __name__ == "__main__":

	# Get list of mood tags
	ftags = open("../data/tags-of-interest.txt", "r")
	tags = [x.rstrip() for x in ftags.readlines()]
	columns_of_interest = ["clip_id"] + tags + ["mp3_path"]


	# Initialize pandas dataframe with mood columns only
	annotations = pd.read_csv("../data/annotations.csv")
	annotations = annotations[columns_of_interest]


	# Remove rows without any mood tag
	annotations["mood_count"] = annotations.apply(lambda row: mood_count(row, tags), axis=1)
	annotations = annotations[annotations["mood_count"] != 0]
	print(annotations.count)
	# print(annotations.tail(10))