#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :9/16/18 4:10 PM
#@Author  :Jie Liu 
#@FileName: pathpuzzle.py
#@Software: PyCharm



from puzzleconfig.citynode import citynode
import sys
import math
class pathpuzzle(object):

     def __init__(self, filecontent, heuristicfunction = None):

         self.filecontent = filecontent
         self.allcitynodes = []
         self.childnodes = []
         self.hn = heuristicfunction
         self.pathcosttochild = dict()
         self.initialstate = eval(filecontent[2])
         self.goalstate = eval(filecontent[3])

         for node in eval(filecontent[1]):
             self.addcitynode(node[0], (node[1], node[2]))

#         for i in self.allcitynodes:            
#             for child in i.childnodes:
#                 print child.state

         self.initialnode = self.retrivenodes(self.initialstate)
         self.goalnode = self.retrivenodes(self.goalstate)

     def generatechildnodes(self, node):
         for content in self.filecontent[4:]:
             pairwisenodes = eval(content)
             if node.state == pairwisenodes[0]:
                 secondnode = self.retrivenodes(pairwisenodes[1])
                 if node.state != secondnode.state:
                     secondnode.parent = node
                     if secondnode not in node.childnodes:
                        node.childnodes.append(secondnode)
                        node.pathcosttochild[secondnode] = pairwisenodes[2]

             if node.state == pairwisenodes[1]:
                 firstnode = self.retrivenodes(pairwisenodes[0])
                 if node.state != firstnode.state:
                     firstnode.parent = node
                     if firstnode not in node.childnodes:
                        node.childnodes.append(firstnode)
                        node.pathcosttochild[firstnode] = pairwisenodes[2]
         return node.childnodes


     def addcitynode(self, state, location, isgoal = False):
         node = citynode(state, location, parent= None, isgoal=None)
         self.allcitynodes.append(node)
         return self.allcitynodes


     def retrivenodes(self, name):
         for node in self.allcitynodes:
             if node.state == name:
                 return node

         return None


     def goaltest(self, testnode):
         if testnode.state == self.goalstate:
             return True
         else:
             return False


     def solution(self, node):
         path_back = []
         while node.state != self.initialstate:
             path_back.append(node)
             node = node.parent
             if len(path_back) > 50:
                 break
         return list(reversed(path_back))

     def getbestcosttochild(self, node):

         cost = sys.maxint
         childlist = self.generatechildnodes(node)
         for child in node.childnodes:
             if cost > node.pathcosttochild[child]:
                 cost = node.pathcosttochild[child]

         return cost

     def geteuclideandistance(self, node):

         n1 = pow((self.goalnode.location[0] - node.location[0]), 2)
         n2 = pow((self.goalnode.location[1] - node.location[1]), 2)
         n = n1 + n2

         distance = math.sqrt(n)

         return distance

     def getmanhattandistance(self, node):

         n1 = abs(self.goalnode.location[0] - node.location[0])
         n2 = abs(self.goalnode.location[1] - node.location[1])

         distance = n1 + n2

         return distance

     def getdotproductdistance(self, node):

         dotproduct = self.goalnode.location[0]*node.location[0] + self.goalnode.location[1]*node.location[1]

         return dotproduct
     
     def getcosinesimilarity(self, node):
         
         dotproduct = self.goalnode.location[0]*node.location[0] + self.goalnode.location[1]*node.location[1]
             
         squaregoalmode = pow(self.goalnode.location[0], 2) + pow(self.goalnode.location[1], 2)
         goalmode = math.sqrt(squaregoalmode)
         
         squarenodemode = pow(node.location[0], 2) + pow(node.location[1], 2)
         nodemode = math.sqrt(squarenodemode)
         
         similarity = dotproduct / (goalmode * nodemode + 100)
         
         return similarity




