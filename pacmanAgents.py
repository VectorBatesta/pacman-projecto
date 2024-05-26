# pacmanAgents.py
# ---------------
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


from pacman import Directions
from game import Agent
import random
import game
import util

class LeftTurnAgent(game.Agent):
    "An agent that turns left at every opportunity"

    def getAction(self, state):
        legal = state.getLegalPacmanActions()
        current = state.getPacmanState().configuration.direction
        if current == Directions.STOP: current = Directions.NORTH
        left = Directions.LEFT[current]
        if left in legal: return left
        if current in legal: return current
        if Directions.RIGHT[current] in legal: return Directions.RIGHT[current]
        if Directions.LEFT[left] in legal: return Directions.LEFT[left]
        return Directions.STOP

class GreedyAgent(Agent):
    def __init__(self, evalFn="scoreEvaluation"):
        self.evaluationFunction = util.lookup(evalFn, globals())
        assert self.evaluationFunction != None

    def getAction(self, state):
        # Generate candidate actions
        legal = state.getLegalPacmanActions()
        if Directions.STOP in legal: legal.remove(Directions.STOP)

        successors = [(state.generateSuccessor(0, action), action) for action in legal]
        scored = [(self.evaluationFunction(state), action) for state, action in successors]
        bestScore = max(scored)[0]
        bestActions = [pair[1] for pair in scored if pair[0] == bestScore]
        return random.choice(bestActions)

def scoreEvaluation(state):
    return state.getScore()









##################################################################################
##################################################################################
##################################################################################

from util import *
from nodestate_lib import *




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

            #detecta se está repetido em abertos ou fechados
            repetido = False
            for nodeAberto in ABERTOS:
                if filhoGerado.matriz == nodeAberto.matriz: #ja esta em abertos 
                    repetido = True
                    #Se o filho foi alcançado por um caminho mais curto, então:
                    #* de ao estado em ABERTOS o caminho mais curto
                    if filhoGerado.nivel < nodeAberto.nivel:
                        nodeAberto.pai = filhoGerado.pai
                    break

            for nodeFechado in FECHADOS:
                if repetido == True:
                    break

                if filhoGerado.matriz == nodeFechado.matriz: #ja esta em fechados 
                    repetido = True
                    #Se o filho foi alcançado por um caminho mais curto, então:
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
        #pega o nó dos abertos (ou seja, sem filhos) com menor quant de errados
        X = escolheMelhor(ABERTOS) #escolheMelhor dá pop() em ABERTOS
        FECHADOS.append(X)

        atualizaErrados(X, obj)
        
        #se errados == 0, entao é o objetivo!
        if X.errados == 0: 
            return 'SUCESSO', X
        
        listanova = gerar_filhos(X)
        #detecta se nós novos sao repetidos ou sao acima do nivelmax
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
    ABERTOS = [raiz] #é uma pilha
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
    return 'FALHA', None #não restam mais estados


def DFS(raiz: nodeState, objetivo, nivelMax):
    ABERTOS = [raiz] #é uma pilha
    FECHADOS = []
    
    while ABERTOS != []:
        X = ABERTOS.pop() #() = ultimo
        
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
                FECHADOS.append(X)
    return 'FALHA', None #não restam mais estados