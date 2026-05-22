string = input("Enter a word: ")
char = input("Enter a charcacter: ")
count = 0
i = 0
while (i<len(string)):
    if (string[i] == char):
        count = count+1
    i = i+1
print(char,count)        