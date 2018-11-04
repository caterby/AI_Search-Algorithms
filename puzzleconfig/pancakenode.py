#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :9/23/18 5:12 PM
#@Author  :Jie Liu 
#@FileName: pancakenode.py
#@Software: PyCharm

class pancakenode(object):

    def __init__(self, state, parent = None, isgoal = False):

        self.state = state
        self.isgoal = isgoal
        self.childnodes = []
        self.parent = parent
        self.pathcosttochild = dict()
        self.pathcost = 0
        self.totalpathcost = 0


    def getpancakenodestate(self):
        return self.state


    def goaltest(self):
        return self.isgoal

    def getchildnodes(self):
        return self.childnodes


    def getcosttochild(self, childnode):
        if childnode in self.childnodes:
            return self.pathcosttochild(childnode)
        else:
            return None

    def getCost(self, nextnode):
        return 1
