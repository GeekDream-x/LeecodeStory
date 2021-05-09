n = int(input().strip())

while n > 0:

    string = input().strip()
    pair = 0
    curChar = ''
    curCharCount = 0
    i = 0

    while i < len(string):
        char = string[i]

        if char == curChar:
            curCharCount += 1
            if curCharCount == 3:
                # 三连字母 删掉一个
                string = string[0:i] + string[i + 1:]
                curCharCount -= 1
                i -= 1
            elif curCharCount == 2 and pair == 1:
                string = string[0:i] + string[i + 1:]
                curCharCount -= 1
                pair = 0
                i -= 1
        elif char != curChar:
            if curCharCount == 2:
                pair += 1

            curCharCount = 1
            curChar = char
        i += 1

    print(string)
    n -= 1