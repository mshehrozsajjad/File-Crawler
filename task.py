import os
import sys
import ntpath


myPath = 'C:\Users\MuhammadShahroz\Desktop\Advanced Programming'#Setting root path
file_path={}; #Store File path
dir_path={};#store directory path
word_path={};#store word path
choice = ''; # option to change directory


#Creating Index for files
def index_files():
    for root, directory, files in os.walk(myPath):
        for directory1 in directory:
            dir_path[directory1]=[root]
        for file1 in files:
            file_path[file1]=[root]
            if file1.endswith(".txt"):
                with open(root+"\\"+file1,"r")as f:
                    for line in f:
                        
                        for words in line.split():
                        
                            if words in word_path.keys():
                                    print "Same words";
                            else:
                                    word_path[words]=[root+"\\"+file1]
                                    


def check_for_dir(param):
    if param in dir_path.keys():
        return True
    else:
        return False
def check_for_file(param):
    if param in file_path.keys():
        return True
    else:
        return False
def check_for_word(param):
    if param in word_path.keys():
        return True
    else:
        return False


if __name__ == '__main__':
    index_files()
    print "+----------------------------------+";
    print "|           File Crawler           |";
    print "|                                  |";
    print "|  Developed By: Muhammad Shehroz  |";
    print "|          Reg #  111428           |";
    print "+----------------------------------+\n";
    print "Default directory for Searching  "+myPath;
    print "\nWant to change directoy ? (y/n)"
    choice = raw_input()
    if choice == 'y':
        print "Enter new path: ";
        myPath = raw_input()
    print "\nEnter a word to search : ";
    value = raw_input();
    print "\nSearching word in directory names:";
    if check_for_dir(value):
        print "{} is in path :{}".format(value,dir_path[value])
    else:
        print "Not in a Directory.\n";
    print "Searching word in file names:";
    word1=value + ".txt";
    if check_for_file(word1):
        print "{} is in path :{}".format(value,file_path[word1])
    else:
        print "Not in a file.\n";
    print "Searching word inside files:";
    if check_for_word(value):
        print "{} is in path :{}".format(value,word_path[value])
    else:
        print "Not a word inside any file.\n";

    



                        


