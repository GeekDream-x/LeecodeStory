
def replaceSpace(s: str) -> str:

    # 1
    # lis = list(s)
    #
    # for i in range(len(lis)):
    #     if lis[i] == ' ':
    #         lis[i] = '%20'
    # return "".join(lis)

    # 2
    # n = ''
    # for char in s:
    #     if char == ' ': char = '%20'
    #     n += char
    # return n

    # 3
    #return "%20".join(s.split(' '))

    # 4
    return s.replace(" ", "%20")
