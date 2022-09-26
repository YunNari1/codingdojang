with open('words.txt', 'r') as file:
    text = file.readline()
    words= text.split()
    for word in words:
        if 'c' in word:
            print(word.strip(',.'))
