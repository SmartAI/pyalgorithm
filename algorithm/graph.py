#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 上午10:21
# @Author  : simon
# @File    : graph


import collections


class Graph(object):
    def __init__(self, d=None):
        if d is not None:
            self.graph = d
        else:
            self.graph = collections.defaultdict(set)

    def add_edge(self, u, v):
        self.graph[u].add(v)

    def bfs(self, s):
        visited, queue = set(), [s]
        while queue:
            v = queue.pop(0)
            if v not in visited:
                visited.add(v)
                queue.extend(self.graph[v] - visited)
        return visited

    def bfs_path(self, s, g):
        queue = [(s, [s])]
        while queue:
            v, path = queue.pop(0)
            for next in self.graph[v] - set(path):
                if next == g:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))

    def dfs(self, s):
        return self._dfs(s, set())

    def _dfs(self, s, visited):
        visited.add(s)
        for next in self.graph[s] - visited:
            self._dfs(next, visited)
        return visited

    def dfs_path(self, s, g, path=None):
        if path is None:
            path = [s]
        if s == g:
            yield path
        for next in self.graph[s] - set(path):
            yield from self.dfs_path(next, g, path + [next])

    def shortest_path(self, s, g):
        try:
            return next(self.bfs_path(s, g))
        except StopIteration:
            return None


if __name__ == '__main__':
    d = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])}
    graph = Graph(d)
    print(list(graph.dfs_path('C', 'F')))
    print(graph.bfs('A'))
    print(list(graph.bfs_path('F', 'D')))
    print(graph.shortest_path('F', 'D'))
