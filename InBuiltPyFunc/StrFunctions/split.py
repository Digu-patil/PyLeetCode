def split_func(str_val: str, delimiter = None):
    '''
    This function will create a list based on the input string and the provided delimiter
    i.e., 'geeks for geeks' with delimiter = ' ' will return ['geeks', 'for', 'geeks']
    '''
    if delimiter is None:
        delimiter = ' '
    start = 0
    end = 0
    str_len = len(str_val)
    ls = []
    while end < str_len:
        if str_val[end] == delimiter:
            if start != end:
                ls.append(str_val[start:end])
            start = end + 1
        end += 1
    if str_val[start:end]:
        ls.append(str_val[start:end])
    return ls


if __name__ == '__main__':
    print(split_func('geeks for geeks'))
    print(split_func('geeks         for       geeks       '))


