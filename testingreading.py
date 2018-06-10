import os, sys, fnmatch

while len(sys.argv) != 2:
	print("Usage: python tac.py <validation_dir>")

os.chdir(sys.argv[1])

imageList = []
fileList = []
for file in os.listdir():
	if fnmatch.fnmatch(file, "*.jpg"):
		imageList.append(file)
	if fnmatch.fnmatch(file, "*.jpeg.txt")
		fileList.append(file)

#print(imageList)

os.chdir("..")

for image in imageList:
	os.system("python label_image.py "+ sys.argv[1] + "/" + str(image))
