#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :9/16/18 4:56 PM
#@Author  :Jie Liu 
#@FileName: greedysearch.py
#@Software: PyCharm
import sys
from puzzleconfig.iterablePQ import iterablePQ
#from puzzleconfig.astarPE import iterablePQ
class greedysearch(object):

    def greedy(self, puzzletype):

        costheuristic = lambda node: puzzletype.hn(node)
        solutionlist, generatednodes, maxfrontiersize, exploredlistlength = self.bestfirstseaech(puzzletype, costheuristic)

        return solutionlist, generatednodes, maxfrontiersize, exploredlistlength

    def bestfirstseaech(self, puzzletype, costheuristic):

        costfn = costheuristic
        startnode = puzzletype.initialnode
        startnode.pathcost = 0
        generatednodes = 0
        frontier = iterablePQ(startnode, costfn)
        maxfrontiersize = len(frontier)
        solutionpath = []
        explored = set()

        if puzzletype.goaltest(startnode):
            return [], generatednodes, maxfrontiersize, len(explored)

        while frontier:

            if len(frontier) == 0:
                print("The frontier is empty")
                exit(1)

            node = frontier.pop()
            print("check the node poped from the frontier:")
            print node.state

            solutionpath.append(node)

            if puzzletype.goaltest(node):
                
                return solutionpath, generatednodes, maxfrontiersize, len(explored)

            explored.add(node.state)
            childnodeslist = puzzletype.generatechildnodes(node)
#            print("The child nodes for the poped node in the frontier:")
#            for child in node.childnodes:
#                print child.state

            generatednodes += len(childnodeslist)

            for child in childnodeslist:

                if child not in frontier and child.state not in explored:
                    frontier.add(child)
                 #   child.pathcost = node.pathcost + node.pathcosttochild[child]

            if maxfrontiersize < len(frontier):
                maxfrontiersize = len(frontier)
