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



from util import *
from searchTestClasses import GraphSearch


def depthFirstSearch(problem):
    raiz = (problem.getStartState(), [])
    print "Node:", raiz
    print "Node eh objetivo?", problem.isGoalState(raiz[0])
    print "Filhos de node:", problem.getSuccessors(raiz[0])

    ABERTOS = Stack()
    ABERTOS.push(raiz) #eh uma pilha
    FECHADOS = Stack()
    
    while ABERTOS.isEmpty() != False:
        X = ABERTOS.pop() #() = ultimo
        FECHADOS.push(X)
        
        if problem.isGoalState(X[0]):
            return X[1]
        else:
            ListaFilhos = problem.getSucessors(X[0])
            
            for node in ListaFilhos:
                if node in ABERTOS:
                    ListaFilhos.remove(node) #evita ciclos ou loops
                if node in FECHADOS:
                    ListaFilhos.remove(node) #evita ciclos ou loops
            
            for node in ListaFilhos:
                ABERTOS.push((node[0], X[1] + [node[1]])) #enfileirar os estados na pilha
    ######################
    return None

def breadthFirstSearch(problem):
    raiz = (problem.getStartState(), [])

    ABERTOS = Queue() #eh uma fila
    ABERTOS.push(raiz)
    FECHADOS = Queue()

    while ABERTOS.isEmpty != True:
        X = ABERTOS.pop() #= primeiro
        FECHADOS.push(X[0])
        
        if problem.isGoalState(X[0]) == True:
            return X[1]
        else:
            ListaFilhos = problem.getSuccessors(X[0])
            
            for node in ListaFilhos:
                if node in ABERTOS:
                    ListaFilhos.remove(node) #evita ciclos ou loops
                if node in FECHADOS:
                    ListaFilhos.remove(node) #evita ciclos ou loops
                    
            for node in ListaFilhos:
                ABERTOS.push((node[0], X[1] + [node[1]])) #enfileirar os estados na Fila
    ######################
    return None

def uniformCostSearch(problem):
    raiz = (problem.getStartState(), [], 0)

    ABERTOS = PriorityQueue()
    ABERTOS.push(raiz, 0)
    FECHADOS = Queue()

    while ABERTOS.isEmpty != True:
        X = ABERTOS.pop()
        
        if problem.isGoalState(X[0]): 
            return X[1]

        if X[0] not in FECHADOS:
            FECHADOS.add(X[0])

            ListaFilhos = problem.getSuccessors(X[0])

            for node in ListaFilhos:
                if node[0] not in FECHADOS:
                    heuristica = X[2] + node[2]
                ABERTOS.push((node[0], X[1] + [node[1]], heuristica), heuristica)
        #############
    return None

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    raiz = (problem.getStartState(), [], 0)

    ABERTOS = PriorityQueue()
    ABERTOS.push(raiz, 0)
    FECHADOS = Queue()

    while ABERTOS.isEmpty != True:
        filhoAtual = ABERTOS.pop()

        if problem.isGoalState(filhoAtual[0]):
            return filhoAtual[1]

        #################
        if filhoAtual[0] not in FECHADOS:
            FECHADOS.push(filhoAtual[0])
            
            ListaFilhos = problem.getSuccessors(filhoAtual[0])

            for node in ListaFilhos:
                if node[0] not in FECHADOS:
                    heuristica_custos = []

                    heuristica_custos.append(filhoAtual[2] + node[2]) #custo f ou g
                    heuristica_custos.append(heuristica_custos[0] + heuristic(node[0], problem)) #custo total

                    ABERTOS.push((node[0], filhoAtual[1] + [node[1]], heuristica_custos[0]), heuristica_custos[1])
                    #dupla/tupla
        ######################
    return None



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
