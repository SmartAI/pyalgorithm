#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 下午2:47
# @Author  : simon
from unittest import TestCase
from algorithm.bloomfilter import BloomFilter as BF


# @File    : test_bloomFilter
class TestBloomFilter(TestCase):
    def setUp(self):
        self.bf = BF(20, 0.05)
        word_present = ['abound', 'abounds', 'abundance', 'abundant', 'accessable',
                        'bloom', 'blossom', 'bolster', 'bonny', 'bonus', 'bonuses',
                        'coherent', 'cohesive', 'colorful', 'comely', 'comfort',
                        'gems', 'generosity', 'generous', 'generously', 'genial']

        for w in word_present:
            self.bf.add(w)

    def test_add(self):
        self.assertEqual(True, self.bf.check("colorful"))
        self.assertEqual(True, self.bf.check("comely"))
        self.assertEqual(True, self.bf.check("comfort"))
        self.assertEqual(False, self.bf.check("test"))
        self.assertEqual(False, self.bf.check("smart"))
        self.assertEqual(False, self.bf.check("boom!"))

