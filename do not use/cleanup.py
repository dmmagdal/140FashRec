# cleanup.py
# removes any non appropriately labeled files for cs140 project
# and reformats image label txt files

import os, sys


# check if there are a correct number of sys args
if len(sys.argv) != 2:
	print("Syntax: python cleanup.py <directory>")
	sys.exit(0)

directory = sys.argv[1]

# check if directory exists
if not os.path.exists(directory):
	print("Target <directory> does not exist.")
	sys.exit(0)


fileslist = os.listdir(directory)
#print(fileslist)
#print(len(fileslist))

#chande directory
os.chdir(directory)

# scan through the directory
for i in range(1, (len(fileslist)//2)+1):
	# modify txt files to format contents correctly
	try:
		txtfile = open("id_%s.txt" %i, 'r')
		textlist = []
		for line in txtfile:
			textlist.append(line)
		#print(textlist)
		# if the txt files are line by line rather than a sinlge line
		if len(textlist) != 1:
			# join each line together into 1 list and merge the elements
			for j in range(len(textlist)):
				textlist[j] = textlist[j][0:1]
			textlist[:] = ["".join(textlist[:])]
			# open the file and write the changes
			txtfile2 = open("id_%s.txt" %i, 'w')
			txtfile2.write(textlist[0])
			txtfile2.close()
		#print(textlist)
		# parse the list so that it only give digits
		txtfile.close()
	except FileNotFoundError:
		pass