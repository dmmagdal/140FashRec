import os


os.chdir("image_labels_dir")

directList = os.listdir()
for i in directList:
	splitString = i.split(".")
	newFileName = splitString[0] + ".jpg.txt"
	os.rename(i, newFileName)