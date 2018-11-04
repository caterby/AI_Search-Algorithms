#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :9/16/18 4:52 PM
#@Author  :Jie Liu 
#@FileName: breadthfirstsearch.py
#@Software: PyCharm

import collections
class breadthfirstsearch(object):

    def bfs(self, puzzletype):

        startnode = puzzletype.initialnode
        generatednodes = 0
        frontier = collections.deque([startnode])
        maxfrontiersize = len(collections.deque([startnode]))
        explored = set()
        solutionpath = []
        
        if puzzletype.goaltest(startnode):
            return [], generatednodes, maxfrontiersize, len(explored)

        while frontier:

            node = frontier.pop()
            explored.add(node.state)
            solutionpath.append(node)
            
            childnodeslist = puzzletype.generatechildnodes(node)           

            generatednodes += len(childnodeslist)

            for child in childnodeslist:

                if child not in frontier and child.state not in explored:
                    if puzzletype.goaltest(child):                       
                        return solutionpath, generatednodes, maxfrontiersize, len(explored)
                    else:
                        frontier.append(child)

                    if maxfrontiersize < len(frontier):
                        maxfrontiersize = len(frontier)