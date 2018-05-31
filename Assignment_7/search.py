"""
search.py: Search algorithms on grid.
"""


def heuristic(a, b):
    """
    Calculate the heuristic distance between two points.

    For a grid with only up/down/left/right movements, a
    good heuristic is manhattan distance.
    """

    # BEGIN HERE #

    return abs(a[0]-b[0])+abs(a[1]-b[1])

    # END HERE #


def searchHillClimbing(graph, start, goal):
    """
    Perform hill climbing search on the graph.

    Find the path from start to goal.

    @graph: The graph to search on.
    @start: Start state.
    @goal: Goal state.

    returns: A dictionary which has the information of the path taken.
             Ex. if your path contains and edge from A to B, then in
             that dictionary, d[B] = A. This means that by checking
             d[goal], we obtain the node just before the goal and so on.

             We have called this dictionary, the "came_from" dictionary.
    """

    # Initialise the came_from dictionary
    came_from = {}
    came_from[start] = None

    # BEGIN HERE #
    if start==goal:
    	return came_from
    visited={}
    parent={}
    stack=[]
    stack.append(start) 
    visited[start]=1
    current=None
    while(len(stack)):
    	next_node = stack.pop()
    	if next_node == goal:
    		break
    	current=next_node
    	sc_neighbors=sorted([[heuristic(x,goal),x] for x in graph.neighboursOf(current)])
    	for h,neighbor in sc_neighbors[::-1]:
    		if neighbor == goal:
    			parent[neighbor]=current
    		if not visited.get(neighbor,0):
    			visited[neighbor]=1
    			parent[neighbor]=current
    			stack.append(neighbor)
    if goal not in parent.keys():
    	return came_from
    temp=goal
    while(1):
    	came_from[temp]=parent[temp]
    	temp=parent[temp]
    	if(temp==start):
    		return came_from
    # END HERE #

    return came_from


def searchBestFirst(graph, start, goal):
    """
    Perform best first search on the graph.

    Find the path from start to goal.

    @graph: The graph to search on.
    @start: Start state.
    @goal: Goal state.

    returns: A dictionary which has the information of the path taken.
             Ex. if your path contains and edge from A to B, then in
             that dictionary, d[B] = A. This means that by checking
             d[goal], we obtain the node just before the goal and so on.

             We have called this dictionary, the "came_from" dictionary.
    """


    # Initialise the came_from dictionary
    came_from = {}
    came_from[start] = None


    # BEGIN HERE #
    import heapq
    if start==goal:
    	return came_from
    visited={}
    parent={}
    pq=[]
    pq.append((heuristic(start,goal),start)) 
    visited[start]=1
    heapq.heapify(pq)
    current=None
    while(len(pq)):
    	next_node = heapq.heappop(pq)[1]
    	if next_node == goal:
    		break
    	current=next_node
    	c_neighbors = graph.neighboursOf(current)
    	for neighbor in c_neighbors:
    		if not visited.get(neighbor,0):
    			parent[neighbor]=current
    			visited[neighbor]=1
    			heapq.heappush(pq,(heuristic(neighbor,goal),neighbor))
    if goal not in parent.keys():
    	return came_from
    temp=goal
    while(1):
    	came_from[temp]=parent[temp]
    	temp=parent[temp]
    	if(temp==start):
    		return came_from
    # END HERE #

    return came_from



def searchBeam(graph, start, goal, beam_length=3):
    """
    Perform beam search on the graph.

    Find the path from start to goal.

    @graph: The graph to search on.
    @start: Start state.
    @goal: Goal state.

    returns: A dictionary which has the information of the path taken.
             Ex. if your path contains and edge from A to B, then in
             that dictionary, d[B] = A. This means that by checking
             d[goal], we obtain the node just before the goal and so on.

             We have called this dictionary, the "came_from" dictionary.
    """

    # Initialise the came_from dictionary
    came_from = {}
    came_from[start] = None

    # BEGIN HERE #
    if start==goal:
    	return came_from
    visited={}
    parent={} 
    visited[start]=1
    curr=[]
    curr.append([heuristic(start,goal),start])
    while(len(curr)):
    	beam=set()
    	for h,par in curr:
    		for neighbor in graph.neighboursOf(par):
    			if not visited.get(neighbor,0):
    				parent[neighbor]=par
    				beam.add((heuristic(neighbor,goal),neighbor))
    	beam=sorted(list(beam))
    	beam=beam[:min(len(beam),beam_length)]
    	for h,item in beam: 
    		visited[item]=1
    	curr=beam
    if goal not in parent.keys():
    	return came_from
    temp=goal
    while(1):
    	came_from[temp]=parent[temp]
    	temp=parent[temp]
    	if(temp==start):
    		return came_from
    # END HERE #

    return came_from


def searchAStar(graph, start, goal):
    """
    Perform A* search on the graph.

    Find the path from start to goal.

    @graph: The graph to search on.
    @start: Start state.
    @goal: Goal state.

    returns: A dictionary which has the information of the path taken.
             Ex. if your path contains and edge from A to B, then in
             that dictionary, d[B] = A. This means that by checking
             d[goal], we obtain the node just before the goal and so on.

             We have called this dictionary, the "came_from" dictionary.
    """

    # Initialise the came_from dictionary
    came_from = {}
    came_from[start] = None

    # BEGIN HERE #
    import heapq
    if start==goal:
    	return came_from
    visited={}
    parent={}
    pq=[]
    d=0
    pq.append((heuristic(start,goal),start)) 
    visited[start]=1
    heapq.heapify(pq)
    current=None
    while(len(pq)):
    	h,next_node = heapq.heappop(pq)
    	if next_node == goal:
    		break
    	current=next_node
    	c_neighbors = graph.neighboursOf(current)
    	for neighbor in c_neighbors:
    		if neighbor == goal:
    			parent[neighbor]=current
    		if not visited.get(neighbor,0):
    			visited[neighbor]=1
    			parent[neighbor]=current
    			d=h-heuristic(current,goal)+1
    			heapq.heappush(pq,(d+heuristic(neighbor,goal),neighbor))
    if goal not in parent.keys():
    	return came_from
    temp=goal
    while(1):
    	came_from[temp]=parent[temp]
    	temp=parent[temp]
    	if(temp==start):
    		return came_from
    # END HERE #

    return came_from

