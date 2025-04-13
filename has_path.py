'''
write a function, hasPath, that takes in an object representing the adjacency list(hash map) of a directed acyclic graph and two nodes (src,dst). The function should return a boolean indicationg whether or not there exists a directed path between the source and destination nodes


    graph = {
        'f': ['g','i'],
        'g': ['h'],
        'h': [],
        'i': ['g','k'],
        'j': [i],
        'k': []
    }

    hasPath(graph, f, k) # True
'''

'''
traverse graph starting from src: use depthfirst search recursively
if dst found, return true, else false
'''
def hasPathDepthFirst(graph, src, dst):
    if src == dst:
        return True
    return any(hasPath(graph, neighbor, dst) for neighbor in graph[src])
    
    return False

'''
traverse graph starting from src: use breadthfirst search iteratively
if dst found, return true, else false
'''
def hasPathBreadFirst(graph, src, dst):

    queue = [ src ]
    
    while len(queue) > 0:
        current = queue.pop(0)

        if current == dst:
            return True
        [queue.append(neighbor) for neighbor in graph[current]]

    return False

def main():

    graph = {
        'f': ['g','i'],
        'g': ['h'],
        'h': [],
        'i': ['g','k'],
        'j': ['i'],
        'k': []
    }

    # print(hasPathDepthFirst(graph,'f','k'))
    print(hasPathBreadFirst(graph,'f','k'))
    print(hasPathBreadFirst(graph,'g','k'))


if __name__ == "__main__":
    main()
