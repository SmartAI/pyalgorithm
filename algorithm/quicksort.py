#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 下午5:18
# @Author  : simon
# @File    : quicksort


def quicksort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    less = [x for x in a[1:] if x < pivot]
    equal = [x for x in a if x == pivot]
    greater = [x for x in a[1:] if x > pivot]
    return quicksort(less) + equal + quicksort(greater)
