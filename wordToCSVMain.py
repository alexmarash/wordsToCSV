
import csv

def pullWords(letters, inputFile, outputFile, fromMaster):
    inputFile = open(inputFile, "r")
    lines = inputFile.readlines()

    print("input file is read")

    inputFile.close()

    if not fromMaster:
        letters += 1
        #print("test master")

    with open(outputFile, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for line in lines:

            #print ("this line", len(line), letters, fromMaster, " ", line)

            if len(line) == letters:


                #print ("this line2", len(line), " ", line)
                csvwriter.writerow([line])


def main():
    letters = int(input("enter number of letters\n"))
    fromMasterString = input("is this from the master\n")
    inputFile = input("enter input file name\n")
    outputFile = input("enter output file name\n")

    if fromMasterString == 'y' or fromMasterString == 'yes' or \
        fromMasterString == 'Y' or fromMasterString == 'YES':
        fromMaster = True
    else:
        fromMaster = False

    pullWords(letters, inputFile, outputFile, fromMaster)

    print ("complete")

main()