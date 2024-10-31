import heapq

# d stands for distances
# start is the starting node

def djikstra(graph, start):
    d = {node: float('inf') for node in graph}
    d[start] = 0
    pq = [(0, start)]

    while len(pq) > 0:
        
        # the following line removes and returns the smallest item 
        # using "heapq.heappop(pq)" and unpacks the
        # tuple into distance and node
        
        distance, node = heapq.heappop(pq)

        if distance > d[node]:
            continue

        for neighbor, weight in graph[node]: # iterate over neighbors
            new_dist = distance + weight # calculate new distance
            if new_dist < d[neighbor]: # check for shorter path
                d[neighbor] = new_dist # update the shortest distance
                heapq.heappush(pq, (new_dist, neighbor)) # add neighboring node to priority queue

    return d