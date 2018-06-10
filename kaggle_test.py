# kaggle_test.py
# tests the accuracy of the inception net trained graph using the evaluation method used by Kaggle
# looks at the top labels from running the label_image.py script
# author: Mattheo Ioannou

import os, sys, fnmatch


def matchLabels(labelist, resultsLabels, headerForFile, accuracyfile):
    # starting index from the results.txt list for the corresponding file
    startIndex = resultsLabels.index(str(headerForFile + '\n'))
    labels_over_threshold = []
    # counter for number of labels found in top 22
    for i in range(1, len(labelist) + 1):
        # label number from results.txt list
        stringOfLine = resultsLabels[startIndex + i].split(" ")
        # label_score = stringOfLine[3].replace(')\n', '')
        labels_over_threshold.append(stringOfLine[0])
    correct_results = 0
    for l in labels_over_threshold:
        if l in labelist:
            correct_results += 1
    if len(labels_over_threshold) != 0:
        precision = correct_results / len(labels_over_threshold)
        recall = correct_results / len(labelist)
        if precision + recall == 0:
            image_f1_score = 0
        else:
            image_f1_score = 2 * ((precision * recall) / (precision + recall))
    else:
        image_f1_score = 0
    # write the accuracy for the file in the accuracy file
    accuracyfile.write(headerForFile + " accuracy = " + str(image_f1_score * 100) + "%\n")


def main():
    if len(sys.argv) != 2:
        print("Usage: python tac.py <validation_dir>")
        sys.exit(1)

    # move into validation_dir
    os.chdir(sys.argv[1])

    # create list of images and text files in valiation_dir
    imageList = []
    fileList = []
    for file in os.listdir():
        if fnmatch.fnmatch(file, "*.jpg"):
            imageList.append(file)
        if fnmatch.fnmatch(file, "*.jpg.txt"):
            fileList.append(file)

    # return to parent directory
    os.chdir("..")

    # run the command for labeling all images
    # for image in imageList:
    # os.system("python label_image.py " + str(sys.argv[1]) + "/" + str(image))

    # open results.txt to read and create a
    # file to display accuracy per image and
    # total accuracy
    resultsfile = open("results.txt", 'r')
    accuracyfile = open("accuracyfile.txt", 'w')

    # store each line from results.txt to list
    # and store each header string in a list
    resultsLabels = resultsfile.readlines()
    headerStrings = []
    for image in imageList:
        headerStrings.append("**" + str(sys.argv[1]) + "/" + str(image) + "**")

    # iterate through the .jpg.txt files in the file list
    for validfile in fileList:
        file = open(sys.argv[1] + "/" + validfile, 'r')
        headerForFile = headerStrings[
            headerStrings.index(str("**" + str(sys.argv[1]) + "/" + str(validfile).split(".jpg.txt")[0] + ".jpg**"))]
        # store each (valid/ correect) label to a list
        labelList = file.readlines()
        for line in range(len(labelList)):
            labelList[line] = labelList[line].split("\n")[0]
        # print(labelList)
        matchLabels(labelList, resultsLabels, headerForFile, accuracyfile)
        # close the file
        file.close()

    resultsfile.close()
    accuracyfile.close()

    totalacc = open("accuracyfile.txt", 'r')
    acclines = totalacc.readlines()
    count = 0
    for line in acclines:
        if len(line.split(" ")) != 0:
            string = line.split(" ")[3]
            count += float(string.split("%")[0])
    totalaccuracy = count / (len(acclines) - 1)
    print("Total accuracy = " + str(round(totalaccuracy, 2)) + "%")


if __name__ == '__main__':
    main()
