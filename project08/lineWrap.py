"""
File: lineWrap.py
Author: Laurie Jones, Harry Pinkerton, James Lawson
Project: 8

Asks the user to input a file name and a number of characters to linewrap to
creates a new file, named wrap_<filename>.txt,
and writes the words back out to this file
"""




def main():
    intFile = input("What is the name of the text file: ")
    char = int(input("Number of characters to linewrap to: "))
    file1 = open(intFile, "r")
    file2 = open("wrap_" + intFile, "w")

    charCount = open(intFile,'r+').read()
    charCount = len(charCount)
    charCount = charCount//char + 5

    

    for x in range(charCount):
        segment = file1.read(char)
        print(segment)
        file2.write(segment + '\n')

    file1.close()
    file2.close()

if __name__ == '__main__':
    main()
    

