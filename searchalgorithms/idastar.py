#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :9/16/18 4:57 PM
#@Author  :Jie Liu 
#@FileName: idastar.py
#@Software: PyCharm

from Queue import deque
import sys
class idastar(object):

    def idastar(self, puzzletype):
        startnode = puzzletype.initialnode
        print("Start node in the idastar search is: ")
        print startnode.state
        cutoff = puzzletype.hn(startnode) + startnode.pathcost
        limitdepth = cutoff

        while limitdepth < 10000:

           cutoff, solutionlist, generatednodes, maxfrontiersize, exploredlistlength = self.costlimiteddfs(puzzletype, startnode, cutoff)
           limitdepth = cutoff + 1

           if solutionlist is not None:
            return cutoff, solutionlist, generatednodes, maxfrontiersize, exploredlistlength
           if cutoff == sys.maxint:
            print("Fail happens!!!")
            exit(1)


    def costlimiteddfs(self, puzzletype, root, cutoff):

        frontier = deque([root])
        nextcutoff = sys.maxint
        generatednodes = 0
        maxfrontiersize = len(frontier)
        explored = []
        depthlimited = 0
        pathsolution = []

        while frontier:
            if len(frontier) == 0:
                print("Fail happens!!!")
                exit(1)

            node = frontier.pop()
            pathsolution.append(node)
            print("The node poped from the frontier is:")
            print node.state
            depthlimited += 1
            if depthlimited > 100000:
                return nextcutoff, pathsolution, generatednodes, maxfrontiersize, len(explored)
            explored.append(node.state)

            if puzzletype.hn(node) + node.pathcost <= cutoff:
                if puzzletype.goaltest(node):
                    return nextcutoff, puzzletype.solution(node), generatednodes, maxfrontiersize, len(explored)

                childnodeslist = puzzletype.generatechildnodes(node)

                generatednodes += len(childnodeslist)

                for child in node.childnodes:
                    frontier.append(child)

                if maxfrontiersize < len(frontier):
                    maxfrontiersize = len(frontier)
            else:
                if puzzletype.hn(node) + node.pathcost < nextcutoff:
                    nextcutoff = puzzletype.hn(node) + node.pathcost
