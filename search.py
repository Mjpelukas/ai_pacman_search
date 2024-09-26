# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    pacFringe = util.Stack()#store fringe in stack
    currentNode = (problem.getStartState(), [], [])
    pacFringe.push(currentNode)
    closedNodes = []
    #while fringe has elements
    while not pacFringe.isEmpty():
        fringeNode, searchPath, fringeTotal = pacFringe.pop()
        #if get goal state return the path
        if problem.isGoalState(fringeNode):
            return searchPath
        if not fringeNode in closedNodes:
            closedNodes.append(fringeNode)
    			#fill out triple with successor
            for newCoords, newMove, newCost in problem.getSuccessors(fringeNode):
                pacFringe.push((newCoords, searchPath + [newMove], fringeTotal + [newCost]))		
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    pacFringe = util.Queue()#store fringe in queue
    currentNode = (problem.getStartState(), [])
    pacFringe.push(currentNode)
    closedNodes = []
    #while fringe has elements
    while not pacFringe.isEmpty():
        fringeNode, searchPath = pacFringe.pop()
    	#if get goal state return the path
        if problem.isGoalState(fringeNode):
            return searchPath
        if not fringeNode in closedNodes:
            closedNodes.append(fringeNode)
    			#fill out tuple with successor, newcost unused
            for newCoords, newMove, newCost in problem.getSuccessors(fringeNode):
    			#add to the fringe
                pacFringe.push((newCoords, searchPath + [newMove]))		

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #make structures
    pacFringe = util.PriorityQueue()#make fringe prio queue
    pacCount = util.Counter() #make a counter
    currentNode = (problem.getStartState(), [])
    closedNodes = []
    #do initial push
    pacFringe.push(currentNode, 0)
    #while loop for fringe has elements
    while not pacFringe.isEmpty():
        fringeNode, searchPath = pacFringe.pop()
        if problem.isGoalState(fringeNode):
            return searchPath
        if not fringeNode in closedNodes:
            closedNodes.append(fringeNode)
    		#fill out triple with successor
            for newCoords, newMove, newCost in problem.getSuccessors(fringeNode):
                pacCount[newCoords] = pacCount[fringeNode]
                pacCount[newCoords] += newCost
                #add to the fringe queue
                pacFringe.push((newCoords, searchPath + [newMove]), pacCount[newCoords])	#state, plus counts

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    pacFringe = util.PriorityQueue()#make fringe prio queue
    pacCount = util.Counter() #make a counter
    currentNode = (problem.getStartState(), [])
    closedNodes = [] #empty list
    pacCount[str(currentNode[0])] += heuristic(currentNode[0], problem)
    pacFringe.push(currentNode, pacCount[str(currentNode[0])])
    #while elements in fringe
    while not pacFringe.isEmpty():
        fringeNode, searchPath = pacFringe.pop()
    	#if at goal return the path
        if problem.isGoalState(fringeNode):
            return searchPath
        if not fringeNode in closedNodes:
            closedNodes.append(fringeNode)
            for newCoords, newMove, newCost in problem.getSuccessors(fringeNode):
                newPath = searchPath + [newMove]
                pacCount[str(newCoords)] = problem.getCostOfActions(newPath)
                pacCount[str(newCoords)] += heuristic(newCoords, problem)
                pacFringe.push((newCoords, newPath), pacCount[str(newCoords)])	


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
