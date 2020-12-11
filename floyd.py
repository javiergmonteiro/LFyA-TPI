
def floyd_algorithm(G, nV):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))
    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = round(min(distance[i][j], distance[i][k] + distance[k][j]),2)
    #print_solution(distance)
    #print(distance)
    return distance