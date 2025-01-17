import os


def findAverageSentence(filePath, delimiters, minLength):
    file = open(filePath)
    textInFile = file.read()

    words = textInFile.split(" ")
    # print(words)

    # Loop that discludes any words below minimum length - Alexie
    for word in words:
        if len(word) < minLength:
            words.remove(word)
    # End - Alexie
    
    sentences = textInFile.split(".")
    sentences.remove("")

    # print(sentences)
    if (len(sentences) > 0):
        aveSentenceLength = len(words) / len(sentences)
    else:
        aveSentenceLength = words

    return int(round(aveSentenceLength, 0))


def main():
    userFile = input("Enter the file path to the .txt file you wish to analyze.\n")
    isFile = os.path.isfile(userFile)
    while isFile != True:
        print("Enter a valid file")
        userFile = input("Enter the file path to the .txt file you wish to analyze.\n")
        isFile = os.path.isfile(userFile)
        


    userDelimeters = input("Enter the characters (punctuation) that you want to be sentence delimiters separated by spaces.\n")
    userDelimeters = userDelimeters.split(" ")
    minLength = input("Enter the minimum length of a word (must be a positive integer).\n")
    
    minLenPro = ""

    for i in range(len(minLength)):
        # print("1234567890".contains(minLength[i]))
        if (minLength[i] in "1234567890") == False:
            minLenPro = minLenPro + ""
        else:
            minLenPro = minLenPro + minLength[i] 

    print(minLenPro)

    print("The average sentence length is", findAverageSentence(userFile, userDelimeters, minLength))

if __name__ == "__main__":
    main()
