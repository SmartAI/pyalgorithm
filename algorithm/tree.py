#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 下午6:00
# @Author  : simon
# @File    : tree


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self._insert(self.root, data)

    def _insert(self, root, data):
        if self.root is None:
            self.root = Node(data)
            return root
        if root is None:
            root = Node(data)
            return root
        if data <= root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)

        return root


def travel(root):
    if root is not None:
        if root.left is not None:
            travel(root.left)
        print(root.data)
        if root.right is not None:
            travel(root.right)


def binary_search(a, x, l, r):
    if r >= l:
        mid = l + (r - l) // 2
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            return binary_search(a, x, l, mid - 1)
        else:
            return binary_search(a, x, mid + 1, r)
    else:
        return -1
