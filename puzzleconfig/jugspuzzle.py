#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :9/16/18 4:10 PM
#@Author  :Jie Liu 
#@FileName: jugspuzzle.py
#@Software: PyCharm

from puzzleconfig.jugnode import jugnode
import math
class jugspuzzle(object):

     def __init__(self, filecontent, heuristicfunction = None, isgoal = False):

         self.initialstate = eval(filecontent[2])
         self.goalstate = eval(filecontent[3])
         self.childnodes = []
         self.hn = heuristicfunction
         self.firstjugcapacity = eval(filecontent[1])[0]
         self.secondjugcapacity = eval(filecontent[1])[1]
         self.pathcosttochild = dict()
         self.initialnode = jugnode(self.initialstate, isgoal = False)
         self.goalnode = jugnode(self.goalstate, isgoal = True)


     def generatechildnodes(self, node):

         x = node.state[0]
         y = node.state[1]
         if x < 3:
             childnode = jugnode((3, y))
             if childnode.state != node.state:
                childnode.parent = node
                node.pathcosttochild[childnode] = 1
                node.childnodes.append(childnode)
         if y < 4:
             childnode = jugnode((x, 4))
             if childnode.state != node.state:
                childnode.parent = node
                node.pathcosttochild[childnode] = 1
                node.childnodes.append(childnode)
         if x > 0:
             childnode = jugnode((0, y))
             if childnode.state != node.state:
                childnode.parent = node
                node.pathcosttochild[childnode] = 1
                node.childnodes.append(childnode)
         if y > 0:
             childnode = jugnode((x, 0))
             if childnode.state != node.state:
                childnode.parent = node
                node.pathcosttochild[childnode] = 1
                node.childnodes.append(childnode)
         if (x + y >= 4) and x > 0:
             childnode = jugnode((x+y-4, 4))
             if childnode.state != node.state:
                childnode.parent = node
                node.pathcosttochild[childnode] = 1
                node.childnodes.append(childnode)
         if (x+y >= 3) and y > 0:
             childnode = jugnode((3, x+y-3))
             if childnode.state != node.state:
                childnode.parent = node
                node.pathcosttochild[childnode] = 1
                node.childnodes.append(childnode)
         if (x+y > 0 and x+y <= 4) and x >= 0:
             childnode = jugnode((0, x+y))
             if childnode.state != node.state:
                childnode.parent = node
                node.pathcosttochild[childnode] = 1
                node.childnodes.append(childnode)
         if (x+y > 0 and x+y <= 3) and y >= 0:
             childnode = jugnode((x+y, 0))
             if childnode.state != node.state:
                childnode.parent = node
                node.pathcosttochild[childnode] = 1
                node.childnodes.append(childnode)

         return node.childnodes


     def goaltest(self, testnode):
         if testnode.state[0] == self.goalstate[0] and testnode.state[1] == self.goalstate[1]:
             return True
         else:
             return False


     def solution(self, node):
         path_back = []
         while node.state != self.initialstate:
             path_back.append(node)
             node = node.parent
         return list(reversed(path_back))

     def geteuclideandistance(self, node):

         n1 = pow((self.goalnode.state[0] - node.state[0]), 2)
         n2 = pow((self.goalnode.state[1] - node.state[1]), 2)
         n = n1 + n2

         distance = math.sqrt(n)

         return distance

     def getmanhattandistance(self, node):

         n1 = abs(self.goalnode.state[0] - node.state[0])
         n2 = abs(self.goalnode.state[1] - node.state[1])

         distance = n1 + n2

         return distance

     def getdotproductdistance(self, node):

         dotproduct = self.goalnode.state[0]*node.state[0] + self.goalnode.state[1]*node.state[1]

         return dotproduct
     
     def getcosinesimilarity(self, node):
         
         dotproduct = self.goalnode.state[0]*node.state[0] + self.goalnode.state[1]*node.state[1]
             
         squaregoalmode = pow(self.goalnode.state[0], 2) + pow(self.goalnode.state[1], 2)
         goalmode = math.sqrt(squaregoalmode)
         
         squarenodemode = pow(node.state[0], 2) + pow(node.state[1], 2)
         nodemode = math.sqrt(squarenodemode)
         
         similarity = dotproduct / (goalmode * nodemode + 100)
         
         return similarity


