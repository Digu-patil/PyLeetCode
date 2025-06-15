'''
Problem Statement
Given a Roman Number we want to convert it to integer
Mapping = {'I':1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D':500, 'M':1000}
'''


def RomanToInteger(r_num):
    Mapping = {'I':1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D':500, 'M':1000}

    #Go through the roman number and store its values in a list
    num_list = []
    for r_char in reversed(r_num):
        num_list.append(Mapping[r_char])

    int_val = num_list[0]
    for i in range(len(num_list)-1):
        if num_list[i] > num_list[i+1]:
            int_val -= num_list[i+1]
        else:
            int_val += num_list[i+1]
    return int_val


'''Test Cases'''
if __name__ == "__main__":
    print(RomanToInteger('XI'))
    print(RomanToInteger('IX'))
    print(RomanToInteger('IV'))
    print(RomanToInteger('VI'))
    print(RomanToInteger('LXVII'))

