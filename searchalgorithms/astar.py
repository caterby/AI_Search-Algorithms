#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :9/16/18 4:56 PM
#@Author  :Jie Liu 
#@FileName: astar.py
#@Software: PyCharm

from puzzleconfig.astarPE import iterablePQ

class astar(object):

    def astar(self, puzzletype):
#        costheuristic = lambda node: puzzletype.hn(node) + node.pathcost
        costheuristic = lambda node: puzzletype.hn(node) + puzzletype.getpathcost(node)
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
        itertimes = 0

        if puzzletype.goaltest(startnode):
            return [], generatednodes, maxfrontiersize, len(explored)

        while frontier:

            if len(frontier) == 0:
                print("The frontier is empty")
                exit(1)

            node = frontier.pop()
            print("check the node poped from the frontier:")
            print node.state
            itertimes += 1
            solutionpath.append(node)
            if puzzletype.goaltest(node):
                print("The goal is detected!!!!")
                print("**************************")
                return solutionpath, generatednodes, maxfrontiersize, len(explored)

            explored.append(node.state)

            childnodeslist = puzzletype.generatechildnodes(node)
            
            generatednodes += len(childnodeslist)
            
            if itertimes > 10000:
                return solutionpath, generatednodes, maxfrontiersize, len(explored)
                break
            
            for child in childnodeslist:

                if child not in frontier and child.state not in explored:
                    frontier.add(child)
                    
                elif child in frontier:
                    currentnode = frontier[child]
                    #child.pathcost = node.pathcost + node.pathcosttochild[child]
                    if frontier.costfn[child] < costfn[currentnode]:
                        frontier.replace(child)
                
                if maxfrontiersize < len(frontier):
                    maxfrontiersize = len(frontier)
