def count_func(main_str, sub_str):
    '''
    This function gives the count of occurence of sub_str in main_str
    '''
    start = 0
    end = len(sub_str)
    ct = 0
    while end <= len(main_str):
        if main_str[start:end] == sub_str:
            ct += 1
        start += 1
        end += 1
    return ct

if __name__ == "__main__":
    print(count_func('geeks for geeks', 'geeks'))