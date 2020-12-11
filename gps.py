from floyd import floyd_algorithm

INF = 999
nV = 8

locations = {
    "a" : 0,
    "b" : 1,
    "c" : 2,
    "e" : 3,
    "d" : 4,
    "f" : 5,
    "g" : 6,
    "h" : 7
}

coordniates = {
    "a" : [-34.774513, -58.267854],
    "b" : [-34.774890, -58.267546],
    "c" : [-34.775390, -58.267235],
    "d" : [-34.775007, -58.267954],
    "e" : [-34.775020, -58.268847],
    "f" : [-34.775357, -58.268756],
    "g" : [-34.775337, -58.267906],
    "h" : [-34.775608, -58.268177]
}

matrix = [
    [0, 3.4, 3.8, 2, INF, INF, INF, INF],
    [3.4, 0, INF, INF, INF, INF, INF, INF],
    [3.8, INF, 0, INF, 3.6, INF, INF, INF],
    [2, INF, INF, 0, 1.8, INF, INF, 4.3],
    [INF, INF, 3.6, 1.8, 0, 1.8, 4, INF],
    [INF, INF, INF, INF, 1.8, 0, INF, INF],
    [INF, INF, INF, INF, 4, INF, 0, INF],
    [INF, INF, INF, 4.3, INF, INF, INF, 0]
]



