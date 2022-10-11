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

def depthFirstSearch(problem: SearchProblem):
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
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    # node ← a node with STATE = problem.INITIAL - STATE, PATH - COST = 0
    node = {'state': problem.getStartState(), 'cost': 0}
    # if problem.GOAL - TEST(node.S TATE) then return S OLUTION(node)
    if problem.isGoalState(node['state']):
        return []
    # frontier ← a LIFO stack with node as the only element
    frontier = util.Stack()
    frontier.push(node)
    # explored ← an empty set
    explored = []
    # loop do
    while(True):
        # if EMPTY ?(frontier) then return failure
        if frontier.isEmpty():
            raise Exception('Search failed -> Frontier is empty')
        # node ← POP(frontier) / * chooses the shallowest node in frontier * /
        node = frontier.pop()
        # add node.S TATE to explored
        explored.append(node['state'])
        # for each action in problem.A CTIONS(node.S TATE) do
        successors = problem.getSuccessors(node['state'])
        for successor in successors:
            # child ← CHILD - NODE(problem, node, action)
            child = {'state': successor[0], 'action': successor[1],
                     'cost': successor[2], 'parent': node}
            # if child .STATE is not in explored or frontier then
            if child['state'] not in explored:
                # if problem.GOAL - T EST(child .STATE) then return SOLUTION(child)
                if problem.isGoalState(child['state']):
                    actions = []
                    node = child
                    while 'parent' in node:
                        actions.append(node['action'])
                        node = node['parent']
                    # But this gives from child to parent -> so we reverse the path
                    actions.reverse()
                    return actions
                # frontier ← I NSERT(child, frontier)
                frontier.push(child)
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    # node ← a node with STATE = problem.INITIAL - STATE, PATH - COST = 0
    node={'state':problem.getStartState(),'cost':0}
    # if problem.GOAL - TEST(node.S TATE) then return S OLUTION(node)
    if problem.isGoalState(node['state']):
        return [] 
    # frontier ← a FIFO queue with node as the only element
    frontier=util.Queue()
    frontier.push(node)
    # explored ← an empty set
    explored=[]
    # loop do
    while(True):
        # if EMPTY ?(frontier) then return failure
        if frontier.isEmpty():
            raise Exception('Search failed -> Frontier is empty')
        # node ← P OP(frontier) / * chooses the shallowest node in frontier * /
        node=frontier.pop()
        # add node.S TATE to explored
        explored.append(node['state'])
        # for each action in problem.A CTIONS(node.S TATE) do
        successors=problem.getSuccessors(node['state'])
        for successor in successors:
            # child ← CHILD - NODE(problem, node, action)
            child={'state':successor[0],'action':successor[1],'cost':successor[2],'parent':node}
            # if child .STATE is not in explored or frontier then
            if child['state'] not in explored:
                # if problem.GOAL - T EST(child .STATE) then return SOLUTION(child)
                if problem.isGoalState(child['state']):
                    actions=[]
                    node=child
                    while 'parent' in node:
                        actions.append(node['action'])
                        node=node['parent']
                    # But this gives from child to parent -> so we reverse the path
                    actions.reverse()
                    return actions
                # frontier ← I NSERT(child, frontier)
                frontier.push(child)
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    # node ← a node with S TATE = problem.I NITIAL - S TATE, P ATH - C OST = 0
    # frontier ← a priority queue ordered by P ATH - C OST, with node as the only element
    # explored ← an empty set
    # loop do
        # if E MPTY ?(frontier) then return failure
        # node ← P OP(frontier) / * chooses the lowest-cost node in frontier * /
        # if problem.G OAL - T EST(node.S TATE) then return S OLUTION(node)
        # add node.S TATE to explored
            # for each action in problem.A CTIONS(node.S TATE) do
                # child ← C HILD - N ODE(problem, node, action)
                # if child .S TATE is not in explored or frontier then
                    # frontier ← I NSERT(child, frontier)
                # else if child .S TATE is in frontier with higher P ATH - C OST then
                    # replace that frontier node with child
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
