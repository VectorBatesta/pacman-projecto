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


"""
def astar(raiz: nodeState, obj):
    ABERTOS = [raiz]
    FECHADOS = []

    while ABERTOS != []:
        filhoAtual = ABERTOS.pop(0)
        printanode(filhoAtual)

        if filhoAtual.matriz == obj:
            return 'SUCESSO', filhoAtual
        
        filhosGerados = gerar_filhos(filhoAtual)

        #################
        for filhoGerado in filhosGerados:
            atualizaErrados(filhoGerado, obj)
            
            #atualiza valor heuristico Fn
            filhoGerado.heuristico = (filhoGerado.errados * 2) + filhoGerado.nivel

            #detecta se esta repetido em abertos ou fechados
            repetido = False
            for nodeAberto in ABERTOS:
                if filhoGerado.matriz == nodeAberto.matriz: #ja esta em abertos 
                    repetido = True
                    #Se o filho foi alcancado por um caminho mais curto, entao:
                    #* de ao estado em ABERTOS o caminho mais curto
                    if filhoGerado.nivel < nodeAberto.nivel:
                        nodeAberto.pai = filhoGerado.pai
                    break

            for nodeFechado in FECHADOS:
                if repetido == True:
                    break

                if filhoGerado.matriz == nodeFechado.matriz: #ja esta em fechados 
                    repetido = True
                    #Se o filho foi alcancado por um caminho mais curto, entao:
                    #* retire o estado de FECHADOS
                    #* adicione o filho em ABERTOS
                    if filhoGerado.nivel < nodeFechado.nivel:
                        FECHADOS.remove(nodeFechado)
                        ABERTOS.append(filhoGerado)
                    break
            
            if repetido == False: #nao esta em fechados ou abertos
                ABERTOS.append(filhoGerado)
        ######################

        FECHADOS.append(filhoAtual)
        ABERTOS.sort(key=lambda x: x.heuristico) #funcao achada no google
    return 'FALHA', None


def heuristica_hill_climbing(raiz: nodeState, obj, nivelmax):
    atualizaErrados(raiz, obj)

    ABERTOS = [raiz]
    FECHADOS = []

    while ABERTOS != []:
        #pega o no dos abertos (ou seja, sem filhos) com menor quant de errados
        X = escolheMelhor(ABERTOS) #escolheMelhor da pop() em ABERTOS
        FECHADOS.append(X)

        atualizaErrados(X, obj)
        
        #se errados == 0, entao eh o objetivo!
        if X.errados == 0: 
            return 'SUCESSO', X
        
        listanova = gerar_filhos(X)
        #detecta se nos novos sao repetidos ou sao acima do nivelmax
        for node in listanova:
            adicionarAbertos = True

            if node.nivel > nivelmax:
                adicionarAbertos = False

            for nodefechado in FECHADOS:
                if node.matriz == nodefechado.matriz:
                    adicionarAbertos = False
            
            for nodeaberto in ABERTOS:
                if node.matriz == nodeaberto.matriz:
                    adicionarAbertos = False

            if adicionarAbertos == True:
                ABERTOS.append(node)
        #############
        printanode(X)



def BFS(raiz: nodeState, objetivo, nivelMax):



def 
"""

from util import *
from searchTestClasses import GraphSearch


def depthFirstSearch(problem):
    raiz = (problem.getStartState(), [])
    print "Node:", raiz
    print "Node eh objetivo?", problem.isGoalState(raiz)
    print "Filhos de node:", problem.getSuccessors(raiz)

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
                ABERTOS.push((node[0], X[1] + [node[1]])) #enfileirar os estados na Fila

def breadthFirstSearch(problem):
        ABERTOS = [raiz] #eh uma pilha
    FECHADOS = []

    while ABERTOS != []:
        X = ABERTOS.pop(0) #(0) = primeiro
        
        printanode(X)
        
        if X.matriz == objetivo:
            return 'SUCESSO', X
        else:
            if X.nivel < nivelMax:
                ListaFilhos = gerar_filhos(X)
                FECHADOS.append(X)
                
                for node in ListaFilhos:
                    for nodeaberto in ABERTOS:
                        if node.matriz == nodeaberto.matriz:
                            ListaFilhos.remove(node) #evita ciclos ou loops
                    for nodefechado in FECHADOS:
                        if node.matriz == nodefechado.matriz:
                            ListaFilhos.remove(node) #evita ciclos ou loops
                        
                for node in ListaFilhos:
                    ABERTOS.append(node) #enfileirar os estados na Fila
            else:
                break
    return 'FALHA', None #nao restam mais estados

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
