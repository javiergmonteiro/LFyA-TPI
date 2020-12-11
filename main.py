from bot import Bot
from gps import coordniates, matrix, locations, nV
from floyd import floyd_algorithm
import threading
import time
import random

task_list = []

def bot_behaviour(bot_number):
    global task_list
    bot = Bot(bot_number)
    while True:
        #print(task_list)
        if task_list and bot.get_state() == 0:
            new_item = task_list.pop()
            bot.change_state("011")
            weight = bot.calculate_trace(matrix, nV, locations[new_item[0]], locations[new_item[1]])
            print("Bot numero {} esta llevando el nuevo item desde {} hasta {}".format(bot.number, new_item[0], new_item[1]))
            bot.change_state("100")
            bot.execute_task(weight)
            bot.change_state("101")
            bot.execute_task(1)
            print("Bot numero {} termino la tarea, regresando".format(bot.number))
            bot.change_state("110")
            bot.execute_task(weight)
            bot.change_state("001")
        else:
            #print("Bot numero {} no encontro ningun item, esperando...".format(bot.number))
            time.sleep(2)

def emulate_items_arrival():
    global task_list
    while True:
        print("Creando nuevo item...")
        item = [random.choice(list(locations.keys())), random.choice(list(locations.keys()))]
        task_list.append(item)
        #print(task_list)
        time.sleep(10)


if __name__ == '__main__':
    for x in range(4):
        print("Creando nuevo bot numero {}".format(x))
        thread = threading.Thread(target=bot_behaviour, args=(x,))
        thread.start()
    
    main_thread = threading.Thread(target=emulate_items_arrival)
    main_thread.start()




