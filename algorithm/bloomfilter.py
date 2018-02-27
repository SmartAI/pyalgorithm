#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 上午11:44
# @Author  : simon
# @File    : bloomfilter


import math
import mmh3
from bitarray import bitarray


class BloomFilter(object):
    def __init__(self, item_count, fp_prob):
        self.fp_prob = fp_prob
        self.size = self._get_size(item_count, fp_prob)
        self.hash_count = self._get_hash_count(self.size, item_count)
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)

    def add(self, data):
        for i in range(self.hash_count):
            digest = mmh3.hash(data, i) % self.size
            self.bit_array[digest] = True

    def check(self, data):
        for i in range(self.hash_count):
            digest = mmh3.hash(data, i) % self.size
            if not self.bit_array[digest]:
                return False
        return True

    @staticmethod
    def _get_size(n, p):
        """
        m = -(n * lg(p)) / (lg(2)^2)
        :param n:
        :param p:
        :return:
        """
        m = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(m)

    @staticmethod
    def _get_hash_count(m, n):
        """
        k = (m/n) * lg(2)
        :param m:
        :param n:
        :return:
        """
        k = (m / n) * math.log(2)
        return int(k)

