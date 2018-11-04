#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :9/16/18 4:53 PM
#@Author  :Jie Liu 
#@FileName: depthfirstsearch.py
#@Software: PyCharm
import collections
import Queue
class depththfirstsearch(object):

    def dfs(self, puzzletype):

        startnode = puzzletype.initialnode
        generatednodes = 0
        frontier = collections.deque([startnode])
        maxfrontiersize = len(collections.deque([startnode]))
        explored = set()
        frontierlist = []

        if puzzletype.goaltest(startnode):
            return puzzletype.solution(startnode), generatednodes, maxfrontiersize, len(explored)

        while frontier:

            node = frontier.popleft()
            print("The node got from the frontier is: ")
            print node.state

            if puzzletype.goaltest(node):
                return puzzletype.solution(node), generatednodes, maxfrontiersize, len(explored)

            explored.add(node.state)
            
            childnodeslist = puzzletype.generatechildnodes(node)

            generatednodes += len(childnodeslist)

            for child in childnodeslist:

                if child not in frontier and child.state not in explored:
                    frontier.appendleft(child)

            if maxfrontiersize < len(frontier):
                maxfrontiersize = len(frontier)
