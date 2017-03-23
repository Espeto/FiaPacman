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
import random
import math

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
    #print "Start: %s" % (problem.getStartState(),)
    #print "Is the start a goal? %s" % (problem.isGoalState(problem.getStartState()),)
    #print "Start's successors: %s" % (problem.getSuccessors(problem.getStartState()),)

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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    start = problem.getStartState()
    board = util.PriorityQueue()
    visited = []
    board.push((start, []), 0)

    while not board.isEmpty():
	    state, actions = board.pop()

	    if problem.isGoalState(state):
		    return actions
			
	    visited.append(state)
		
	    for successor, action, step_cost in problem.getSuccessors(state):
	        if successor not in visited:
			    new_action = actions + [action] 
			    board.push((successor, new_action), problem.getCostOfActions(new_action))
			
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    board = util.PriorityQueue()
    visited = []
    start = problem.getStartState()
    board.push((start, []), heuristic(start,problem))
	
    while not board.isEmpty():
	    state, actions = board.pop()
		
	    if problem.isGoalState(state):
		    return actions
			
	    visited.append(state)
			
	    for successor, action, step_cost in problem.getSuccessors(state):
		    if successor not in visited:
			    new_action = actions + [action]
			    cost = step_cost + heuristic(successor, problem)
			    board.push((successor, new_action), cost)
	
    return []
    
	
def hillClimbingSearch(problem, heuristic = nullHeuristic):
	current = problem.getStartState()
	current_cost = heuristic(current, problem)
	actions = []
	
	while True:
		
		successors = problem.getSuccessors(current)
		better_state = successors[0][0]
		better_cost = successors[0][2] + heuristic(better_state, problem)
		new_action = successors[0][1]
	
		#Get the better valued successor
		for successor, action, step_cost in successors:
			if step_cost + heuristic(successor, problem) < better_cost:
				better_state = successor
				new_action = action
				better_cost = step_cost + heuristic(successor, problem)
		
		if	better_cost > current_cost:
			return actions
			
		current = better_state
		current_cost = better_cost
		actions.append(new_action)
		
	return []

def simuAnnealSearch(problem, heuristic = nullHeuristic):
	temp = 10000
	cooling_rate = 0.003
	current = problem.getStartState()
	current_cost = heuristic(current, problem)
	actions = []
	
	while True:
		temp = temp * (1-cooling_rate)
		
		if temp < 1:
			return actions
			
		successors = problem.getSuccessors(current)
		successor, action, step_cost = successors[random.randint(0, len(successors)-1)]
		
		successor_cost = step_cost + heuristic(successor, problem)
		
		delta_E = successor_cost - current_cost
		
		if delta_E > 0:
			current = successor
			current_cost = successor_cost
			actions.append(action)
			
		elif math.exp(delta_E / temp) > 0.8:
			current = successor
			current_cost = successor_cost
			actions.append(action)
		
	return []		
	
	
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
sas = simuAnnealSearch
hcs = hillClimbingSearch
