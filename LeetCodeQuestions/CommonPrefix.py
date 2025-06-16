'''
Problem Statement - 
Find the Largest Common Prefix given a list of strings
'''

def CommonPrefix(str_list):
    if len(str_list) == 0:
        return ''
    if len(str_list) == 1:
        return str_list[0]
    str_list.sort()

    i = 0
    req_list = []
    while i < len(str_list[0]):
        if str_list[0][i] == str_list[-1][i]:
            req_list.append(str_list[0][i])
        else:
            break
        i+=1
    return ''.join(req_list)


'''Test Case'''
if __name__ == "__main__":
    print(CommonPrefix(["flower","flow","flight"]))
    print(CommonPrefix(["dog","racecar","car"]))
    print(CommonPrefix(["flower"]))
    print(CommonPrefix(["",""]))

