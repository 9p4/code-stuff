import os
def findPics():
    global counter
    global dcounter
    counter = 0
    dcounter = 0
    f = open("files.txt", "w")
    rootDir = input("Enter Directory: ")
    for dirName, subdirList, fileList in os.walk(rootDir):
        print("Found directory: " + dirName)
        thing = dirName + "\n"
        dcounter = dcounter + 1
        f.write(thing)
        for fname in fileList:
            print("\tFound file: " + fname)
            thing = fname + "\n"
            counter = counter + 1
            f.write(thing)
    f.close()
global counter
global dcounter
findPics()
print("Total Folders: " + str(dcounter))
print("Total Files: " + str(counter))
print("Wrote output to 'files.txt'")