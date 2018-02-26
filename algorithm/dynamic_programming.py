#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 上午11:07
# @Author  : simon
# @File    : dynamic_programming


import sys


# Primitive Calculator
# 给定一个正整数 n 得到从1开始要么
# +1 *2 * 3 用最少步数达到n
def min_ops(n):
    result = [0] * (n + 1)
    for i in range(2, n + 1):
        min1 = result[i - 1]
        min2, min3 = sys.maxsize, sys.maxsize
        if i % 2 == 0:
            min2 = result[i // 2]
        if i % 3 == 0:
            min3 = result[i // 3]
        min_op = min(min1, min2, min3)
        result[i] = min_op + 1

    return result


def construct_min_list(n, ops):
    sequence = []
    while n > 0:
        sequence.append(n)
        if n % 2 != 0 and n % 3 != 0:
            n = n - 1
        elif n % 2 == 0 and n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            if ops[n - 1] < ops[n // 2]:
                n = n - 1
            else:
                n = n // 2
        elif n % 3 == 0:
            if ops[n - 1] < ops[n // 3]:
                n = n - 1
            else:
                n = n // 3
    return list(reversed(sequence))


def primitive_calculator(n):
    if n == 1:
        return 1, [1]
    else:
        ops = min_ops(n)
        return ops[-1], construct_min_list(n, ops)


def knapsack_origin(W, wt, val, n):
    if W == 0 or n == 0:
        return 0
    if wt[n - 1] > W:
        return knapsack(W, wt, val, n - 1)
    else:
        return max(knapsack(W, wt, val, n - 1),
                   knapsack(W - wt[n - 1], wt, val, n - 1) + val[n - 1])


def knapsack(W, wt, val, n):
    dp_result = [[0 for i in range(W + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for weight in range(1, W + 1):
            dp_result[i][weight] = dp_result[i - 1][weight]
            if wt[i - 1] <= weight:
                tmp = dp_result[i - 1][weight - wt[i - 1]] + val[i - 1]
                if tmp > dp_result[i][weight]:
                    dp_result[i][weight] = tmp
    return dp_result[n][W]


def edit_distance(s, t):
    dp_result = [[i for i in range(len(s) + 1)] for j in range(len(t) + 1)]
    for i in range(len(t) + 1):
        dp_result[i][0] = i

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            insert_op = dp_result[j - 1][i] + 1
            delete_op = dp_result[j][i - 1] + 1
            match_op = dp_result[j - 1][i - 1]
            mismatch_op = match_op + 1
            if s[i - 1] == t[j - 1]:
                dp_result[j][i] = min(insert_op, delete_op, match_op)
            else:
                dp_result[j][i] = min(insert_op, delete_op, mismatch_op)

    return dp_result[len(t)][len(s)]
