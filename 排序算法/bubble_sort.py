# coding: utf-8

import numpy as np

alist = []
def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(0, n-1):
        for i in range(0, n-1-j):
            # 代表下标从头到位
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1], alist[i]
                count += 1
        if 0 == count:
            return

if __name__ == "__main__":
    li = np.random.randint(100, size = 10)
    print(li)
    bubble_sort(li)
    print(li)

