#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :9/16/18 4:55 PM
#@Author  :Jie Liu 
#@FileName: iteradeepdfs.py
#@Software: PyCharm

import collections
import sys
class iteradeepdfs(object):

    def iddfs(self, puzzletype):


        for depth in xrange(sys.maxint):
            solution, generatednodes, maxfrontiersize, exploredlistlength = self.depthlimitedsearch(puzzletype)
            if generatednodes:
                return solution, generatednodes, maxfrontiersize, exploredlistlength


    def depthlimitedsearch(self, puzzletype, limit = -1):

        startnode = puzzletype.initialnode
        generatednodes = 0
        frontier = collections.deque([startnode])
        maxfrontiersize = len(collections.deque([startnode]))
        explored = []
        cutoff = 'cutoff'
        cutoffoccurred = None
        depthlimited = 0
        solutionpath = []

        while frontier:

            node = frontier.popleft()
            print("The node got from the frontier is: ")
            print node.state
            depthlimited += 1
            
            if depthlimited > 100000:
                return solutionpath, generatednodes, maxfrontiersize, len(explored)
            
            if puzzletype.goaltest(node):
                return solutionpath, generatednodes, maxfrontiersize, len(explored)
            elif limit >= 0:
                cutoff_occurred = True
                limit += 1
               
            nodestate = node.state
                    
            explored.append(node.state)
            solutionpath.append(node)
            childnodeslist = puzzletype.generatechildnodes(node)

            generatednodes += len(childnodeslist)

            for child in childnodeslist:

                if child not in frontier and child.state not in explored:
                    frontier.appendleft(child)

            if maxfrontiersize < len(frontier):
                maxfrontiersize = len(frontier)

            for node in frontier:
                limit -= 1
                



