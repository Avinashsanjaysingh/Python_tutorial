# Write a python function to remove a given word from a list and strip it at the same time.


wordList = ["apple", " banana", "orange ", "apple  ", "  grape", "apple"]
wordToRemove = "apple"

def removeAndStrip(wordToRemove,wordList):
    list = []
    newList = []
    for i in range(len(wordList)):
        list.insert(i,wordList[i].strip())

    for i in range(len(wordList)):
        if list[i] != wordToRemove :
            newList.append(list[i])
    return newList

print(removeAndStrip(wordToRemove,wordList))

