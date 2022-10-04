"""
Use these two functions to find the left and right bounds of the character "|"" 

Credit to stackoverflow post

https://stackoverflow.com/questions/1883980/find-the-nth-occurrence-of-substring-in-a-string
"""


def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


# Create an array for all the names
names = []

# Open up our file name in question
filename = 'raw_data/ind_2017-2018.txt'
with open(filename, 'rt') as myFile:
    for myLine in myFile:
        leftMarker = find_nth(myLine, "|", 7)
        rightMarker = find_nth(myLine, "|", 8)
        formattedNames = myLine[leftMarker+1:rightMarker]
        names.append(formattedNames)

        # Create a new document to save all the formatted names
        with open('formattedNames2017-2018.txt', 'a') as newFile:
            newFile.write(formattedNames)
            newFile.write("\n")

# print(names)
