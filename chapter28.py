with open('words.txt', 'r') as file:
    word = None

    while word != '':
        word = file.readline().strip('\n')
        is_palindrome = True
        for i in range(len(word) // 2):
            if word[i] != word[-1-i]:
                is_palindrome = False
                break
        if is_palindrome:
            print(word)