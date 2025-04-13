
'''
breadth first uses queue
graph is stored as dictionary
solving breadthFirst with recursion is not possible  
define breadthFirst with params graph, source


'''

def breadthFirstIterative(graph, source):
    queue = [ source ]

    while len(queue) > 0:
        current = queue.pop(0)
        print(current)

        [queue.append(neighbor) for neighbor in graph[current]]


# def depthFirstRecursive(graph, source):
#     print(source)
#     [depthFirstRecursive(graph, neighbor) for neighbor in graph[source]]
#
def main():

    graph = {
        'a': ['c','b'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': []
    }

    breadthFirstIterative(graph, 'a')
    # depthFirstIterative(graph, 'a')
    # depthFirstRecursive(graph, 'a')

if __name__ == "__main__":
    main()
