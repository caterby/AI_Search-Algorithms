#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 20:28:21 2018

@author: liujie
"""

from puzzleconfig.iterablePQ import iterablePQ

class pathastar(object):

    def pathastar(self, puzzletype):
        costheuristic = lambda node: puzzletype.hn(node) + node.pathcost
        solutionlist, generatednodes, maxfrontiersize, exploredlistlength = self.bestfirstseaech(puzzletype, costheuristic)

        return solutionlist, generatednodes, maxfrontiersize, exploredlistlength

    def bestfirstseaech(self, puzzletype, costheuristic):

        costfn = costheuristic
        startnode = puzzletype.initialnode
        print("Start node in the astar search is: ")
        print startnode.state
        startnode.pathcost = 0
        generatednodes = 0
        frontier = iterablePQ(startnode, costfn)
        maxfrontiersize = len(frontier)
        explored = []
        solutionpath = []

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

            explored.append(node.state)

            childnodeslist = puzzletype.generatechildnodes(node)
#            print("The child nodes for the poped node in the frontier:")
#            for child in node.childnodes:
#                print child.state

            generatednodes += len(childnodeslist)

            for child in childnodeslist:

                if child not in frontier and child.state not in explored:
                    frontier.add(child)

                elif child in frontier:
                    currentnode = frontier[child]
                    if frontier.costfn[child] < costfn[currentnode]:
                        frontier.replace(child)
                
                if maxfrontiersize < len(frontier):
                    maxfrontiersize = len(frontier)
