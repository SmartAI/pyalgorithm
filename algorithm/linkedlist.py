#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 上午9:35
# @Author  : simon
# @File    : linkedlist


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data)
            tmp = tmp.next

    def reverse(self):
        if self.head is not None:
            self._reverse(self.head, None)

    def _reverse(self, cur, prev):
        if cur.next is None:
            self.head = cur
            cur.next = prev
        else:
            next = cur.next
            cur.next = prev
            return self._reverse(next, cur)
