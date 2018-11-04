#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :9/16/18 4:56 PM
#@Author  :Jie Liu 
#@FileName: unicostsearch.py
#@Software: PyCharm


from puzzleconfig.iterablePQ import iterablePQ
class unicostsearch(object):

    def unicost(self, puzzletype):

        solutionlist, generatednodes, maxfrontiersize, exploredlistlength = self.bestfirstseaech(puzzletype, lambda node: node.pathcost)

        return solutionlist, generatednodes, maxfrontiersize, exploredlistlength

    def bestfirstseaech(self, puzzletype, f):

        costfn = f
        startnode = puzzletype.initialnode
        print("Start node in the unicost search is: ")
        print startnode.state
        startnode.pathcost = 0
        generatednodes = 0
        frontier = iterablePQ(startnode, costfn)
        maxfrontiersize = len(frontier)
        explored = set()
        solutionpath = []

        if puzzletype.goaltest(startnode):
            return [], generatednodes, maxfrontiersize, len(explored)

        while frontier:

            if len(frontier) == 0:
                print("The frontier is empty")
                exit(1)

            node = frontier.pop()
            print("check the node poped from frontier:")
            print node.state
            solutionpath.append(node)
            
            if puzzletype.goaltest(node):
                print("The goal is detected!!!!")
                return solutionpath, generatednodes, maxfrontiersize, len(explored)

            explored.add(node.state)

            childnodeslist = puzzletype.generatechildnodes(node)
            print("The child nodes for the poped node in the frontier:")
            for child in node.childnodes:
                print child.state


            generatednodes += len(childnodeslist)

            for child in childnodeslist:

                if child not in frontier and child.state not in explored:
                    frontier.add(child)
                    child.pathcost = node.pathcost + node.pathcosttochild[child]

                elif child in frontier:
                    child.pathcost = node.pathcost + node.pathcosttochild[child]
                    if frontier.costfn[child] < child.pathcost:
                        frontier.replace(child)

                if maxfrontiersize < len(frontier):
                    maxfrontiersize = len(frontier)









