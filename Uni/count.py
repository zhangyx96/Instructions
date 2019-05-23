import os
import numpy as np


def find_max(sub_path):
    files = os.listdir(sub_path)
    sub_max = 0
    for f in files:
        str = os.path.splitext(f)  
        a = str[0][-3:]
        if str[0][-3:] == 'RGB':
            tmp = str[0][10:14]
            tmp = int(int(tmp)/10)
            sub_max = max(tmp,sub_max) 

    return sub_max


def count_nums(file_path):
    sum = 0
    files = os.listdir(file_path)
    for f in files:
        sub_path = os.path.join(file_path,f)
        if os.path.isdir(sub_path): #is dictionary
            sum += find_max(sub_path)
    return sum


if __name__ == "__main__":
    file_path = os.getcwd()
    imgs_nums = count_nums(file_path)
    print("nums:",imgs_nums)
