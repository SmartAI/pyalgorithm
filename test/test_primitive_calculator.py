#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 上午11:50
# @Author  : simon
from unittest import TestCase
from algorithm import dynamic_programming
from algorithm.dynamic_programming import knapsack
from algorithm.dynamic_programming import edit_distance


# @File    : test_primitive_calculator
class TestPrimitive_calculator(TestCase):
    def test_small(self):
        n = 5
        self.assertEqual((3, [1, 2, 4, 5]), dynamic_programming.primitive_calculator(n))

    def test_large(self):
        n = 96234
        self.assertEqual((14, list(map(int, "1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234".split(' ')))), dynamic_programming.primitive_calculator(n))


class TestKnapsack(TestCase):
    def test_simple(self):
        W = 10
        wt = [1, 4, 8]
        val = [1, 4, 8]
        self.assertEqual(9, knapsack(W, wt, val, len(wt)))

    def test_hard(self):
        val = [60, 100, 120]
        wt = [10, 20, 30]
        W = 50
        self.assertEqual(220, knapsack(W, wt, val, len(wt)))


class TestEditdistance(TestCase):
    def test(self):
        self.assertEqual(3, edit_distance("short", "ports"))

    def test1(self):
        self.assertEqual(1, edit_distance("snowy", "snow"))


