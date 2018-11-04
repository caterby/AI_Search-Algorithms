#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :9/16/18 2:01 PM
#@Author  :Jie Liu 
#@FileName: puzzlesolver.py
#@Software: PyCharm

from puzzleconfig.pathpuzzle import pathpuzzle
from puzzleconfig.jugspuzzle import jugspuzzle
from puzzleconfig.pancakepuzzle import pancakepuzzle
from searchalgorithms.breadthfirstsearch import breadthfirstsearch
from searchalgorithms.depthfirstsearch import depththfirstsearch
from searchalgorithms.iteradeepdfs import iteradeepdfs
from searchalgorithms.unicostsearch import unicostsearch
from searchalgorithms.greedysearch import greedysearch
from searchalgorithms.astar import astar
from searchalgorithms.idastar import idastar
from searchalgorithms.pathastar import pathastar
import sys
import time
import signal

# Global values used to store the information about search algorithms, heuristic functions, and config file names
SEARCHALGORITHM = {'bfs', 'dfs', 'iddfs', 'unicost', 'astar', 'greedy', 'idastar', 'pathastar'}
HEURISTICFUNCTION = {'euclidean', 'manhattan', 'dotproduct', 'cosinesimilarity', 'gapsimilarity'}
CONFIGFILENAME = {'cities', 'jugs', 'pancakes'}

# This function is used for parse the command line and generate a list of arguments
def parseArgument():

    arglist = []
    for arg in sys.argv:
        arglist.append(arg)

    return arglist

# Read the content from the input file
def readfilecontent():
    filecontent = []
    inputfile = sys.argv[1]
    with open(inputfile, "r") as f:
        for line in f:
            line = line.strip('\n')
            print line
            filecontent.append(line)
    f.close()

    return filecontent


def handler(signum, frame):
    print '30 minutes passed, exiting'
    raise Exception("EOP")
    
    
# Main function for the puzzlesolver.py
if __name__ == '__main__':

    signal.signal(signal.SIGALRM, handler)
    signal.alarm(1800)

    try:
     
      argumentlist = parseArgument()
      configfilecontent = readfilecontent()
      solutionpath = []
      exploredlistlength = 0
      numberofnodescreated = 0
      maxfrontierlength = 0

      starttime = time.time()

      if len(argumentlist) < 3 or len(argumentlist) > 4:
          print(" Enter the wrong arguments in the command line")
          exit(1)
      elif len(argumentlist) == 3:
           if configfilecontent[0] not in CONFIGFILENAME or argumentlist[2].lower() not in SEARCHALGORITHM:
              print(" Put the wrong file or algorithm name")
              exit(1)

           elif configfilecontent[0] == 'cities':
               puzzletype = pathpuzzle(configfilecontent)

           elif configfilecontent[0] == 'pancakes':
               puzzletype = pancakepuzzle(configfilecontent)

           if configfilecontent[0] == 'jugs':
               puzzletype = jugspuzzle(configfilecontent)

      elif len(argumentlist) == 4:
          if configfilecontent[0] not in CONFIGFILENAME or argumentlist[2].lower() not in SEARCHALGORITHM or argumentlist[-1].lower() not in HEURISTICFUNCTION:
              print(" Put the wrong file or algorithm or heuristic function")
              exit(1)
          elif configfilecontent[0] == 'cities':
              puzzletype = pathpuzzle(configfilecontent)
          elif configfilecontent[0] == 'pancakes':
              puzzletype = pancakepuzzle(configfilecontent)
          else:
              puzzletype = jugspuzzle(configfilecontent)

      if len(argumentlist) == 4:
         if argumentlist[3].lower() == 'euclidean':
            puzzletype.hn = puzzletype.geteuclideandistance
         elif argumentlist[3].lower() == 'manhattan':
            puzzletype.hn = puzzletype.getmanhattandistance
         elif argumentlist[3].lower() == 'dotproduct':
            puzzletype.hn = puzzletype.getdotproductdistance
         elif argumentlist[3].lower() == 'cosinesimilarity':
            puzzletype.hn = puzzletype.getcosinesimilarity
         elif argumentlist[3].lower() == 'gapsimilarity':
            puzzletype.hn = puzzletype.getgapdistance

      if argumentlist[2].lower() == 'bfs':
          breadthfirst = breadthfirstsearch()
          solutionpath, numberofnodescreated, maxfrontierlength, exploredlistlength = breadthfirst.bfs(puzzletype)
      elif argumentlist[2].lower() == 'dfs':
          depthfirst = depththfirstsearch()
          solutionpath, numberofnodescreated, maxfrontierlength, exploredlistlength = depthfirst.dfs(puzzletype)
      elif argumentlist[2].lower() == 'iddfs':
          iteradeep = iteradeepdfs()
          solutionpath, numberofnodescreated, maxfrontierlength, exploredlistlength = iteradeep.iddfs(puzzletype)
      elif argumentlist[2].lower() == 'unicost':
          unisearch = unicostsearch()
          solutionpath, numberofnodescreated, maxfrontierlength, exploredlistlength = unisearch.unicost(puzzletype)
      elif argumentlist[2].lower() == 'greedy':
          greedysearch = greedysearch()
          solutionpath, numberofnodescreated, maxfrontierlength, exploredlistlength = greedysearch.greedy(puzzletype)
      elif argumentlist[2].lower() == 'astar':
          astar = astar()
          solutionpath, numberofnodescreated, maxfrontierlength, exploredlistlength = astar.astar(puzzletype)
      elif argumentlist[2].lower() == 'pathastar':
          pathastar = pathastar()
          solutionpath, numberofnodescreated, maxfrontierlength, exploredlistlength = pathastar.pathastar(puzzletype)
      elif argumentlist[2].lower() == 'idastar':
          idastar = idastar()
          cutoff, solutionpath, numberofnodescreated, maxfrontierlength, exploredlistlength = idastar.idastar(puzzletype)


      executetime = time.time() - starttime

      print('The execute time of is ' + str(executetime))
      print('Max size of frontier is ' + str(maxfrontierlength))
      print('Number of nodes created is ' + str(numberofnodescreated))
      print('Max number of nodes stored in the explored set is ' + str(exploredlistlength))
      print('Action list is as below: ')
      
      for i in solutionpath:
         print i.state  
      
    except:    
        print("Over 30 minutes!")
    
    finally:
        signal.alarm(0)