#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :9/16/18 4:11 PM
#@Author  :Jie Liu 
#@FileName: jugnode.py
#@Software: PyCharm

class jugnode(object):

    def __init__(self, state, parent = None, isgoal = False):

        self.state = state
        self.isgoal = isgoal
        self.childnodes = []
        self.parent = parent
        self.pathcosttochild = dict()
        self.pathcost = 0
        self.totalpathcost = 0


    def getjugnodestate(self):
        return self.state


    def getfirstjugstate(self):
        return self.currentstate[0]


    def getsecondjugstate(self):
        return self.currentstate[1]


    def goaltest(self):
        return self.isgoal


    def getcosttochild(self, childnode):
        if childnode in self.childnodes:
            return self.pathcosttochild(childnode)
        else:
            return None
