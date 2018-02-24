#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 下午5:23
# @Author  : simon
from unittest import TestCase
from algorithm import quicksort


# @File    : test_quicksort
class TestQuicksort(TestCase):
    def test_normal(self):
        a = [1, 3, 2, 8, 0, 6, 123, 43, 23, 4]
        self.assertEqual(quicksort.quicksort(a), sorted(a))

    def test_same_value(self):
        a = [1, 1, 1, 1, 1]
        self.assertEqual(quicksort.quicksort(a), sorted(a))

    def test_one_elem(self):
        a = [1, 3]
        self.assertEqual(quicksort.quicksort(a), sorted(a))

