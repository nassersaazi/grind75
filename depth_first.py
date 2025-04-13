'''
depth first uses stack
graph is stored as dictionary

define depthFirst with params graph, source

'''

def depthFirstIterative(graph, source):
    stack = [ source ]

    while len(stack) > 0:
        current = stack.pop()
        print(current)

        [stack.append(neighbor) for neighbor in graph[current]]


def depthFirstRecursive(graph, source):
    print(source)
    [depthFirstRecursive(graph, neighbor) for neighbor in graph[source]]

def main():

    graph = {
        'a': ['b','c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': []
    }

    # depthFirstIterative(graph, 'a')
    depthFirstRecursive(graph, 'a')

if __name__ == "__main__":
    main()
