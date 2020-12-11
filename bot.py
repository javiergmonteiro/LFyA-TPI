
import time
from floyd import floyd_algorithm

dfa = {
    0 : {'010':1, '011':2, '101':4},
    1 : {'001':0},
    2 : {'100':3},
    3 : {'101':4},
    4 : {'110':5},
    5 : {'001':0}
}

state_names = {
    0 : 'en reposo',
    1 : 'en acción',
    2 : 'calculando',
    3 : 'en movimiento',
    4 : 'interactuando',
    5 : 'regresando'
}

class Bot:

    def __init__(self, bot_number):
        self.number = bot_number
        self.dfa = dfa
        self.__state = 0

    def get_state(self):
        return self.__state
    
    def change_state(self, next_state):
        try:
            state = self.dfa[self.__state]
            self.__state = state[next_state]
        except KeyError:
            print('codigo {} no existe o no es aceptado por este automata'.format(next_state))
            return
    
    def execute_task(self, modifier):
        print("Bot {} tiempo de la tarea estimado es de {} segundos".format(self.number, 2*modifier))
        time.sleep(2*modifier)
        return
    
    def in_final_state(self):
        if self.__state == 0:
            return True
        else:
            return False
    
    def calculate_trace(self, matrix, nV, first_node, second_node):
        adjacency_matrix = floyd_algorithm(matrix, nV)
        weight = adjacency_matrix[first_node][second_node]
        print("Bot {} encontró el mejor camino con peso de {}".format(self.number, weight))
        return weight
    
    def __str__(self):
        try:
            return state_names[self.__state]
        except Exception as e:
            print(e)
            return
        

    
