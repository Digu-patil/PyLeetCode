def find_func(main_str, sub_str):
    '''
    This function tries to replicat the .find() method 
    This return the index of the first occurence of the sub_str in main_str
    i.e., main_str = 'geeks for geeks', sub_str = 'geeks' this fucntion will return 0 
    '''
    s = 0
    e = len(sub_str)
    main_len = len(main_str)
    sub_len = len(sub_str)
    while s <= main_len - sub_len:
        if main_str[s:e] == sub_str:
            return s
        s += 1
        e += 1
    return -1

if __name__ == '__main__':
    print(find_func('geeks for geeks', 'geeks'))
    print(find_func('nerd geeks for geeks', 'geeks'))
    print(find_func('nerd for geeks', 'geeks'))

