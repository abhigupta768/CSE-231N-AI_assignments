''' class Graph defines the bfs and dfs functions that operate on the graph  '''

class Graph:
	def __init__(self, adj):
		n=len(adj)
		self.graph = dict()
		for i in range(n):
			temp = []
			for j in range(n):
				if adj[i][j]:
					temp.append(j)
			self.graph[i] = set(temp)
	
	def bfs_paths(self, start, goal):
		'''
		Generate and return any path from start to goal using breadth-first search
		Input : start node, goal node
		Output : list of nodes from to be traversed to reach from start to goal(the first node in this list will be the start node and the last node will be the goal node)
		'''
		#BEGIN YOUR CODE HERE
		visited = [0 for _ in range(len(self.graph.keys()))]
		parent={}
		queue=[]
		queue.append(start)
		flag=0
		while(len(queue)):
			s=queue.pop(0)
			visited[s]=1
			for child in self.graph[s]:
				if not visited[child]:
					parent[child]=s
					queue.append(child)
				if child==goal:
					flag=1
					break
			if flag==1:
				break
		temp=goal
		path=[goal]
		for i in range(len(self.graph.keys())):
			path.append(parent[temp])
			temp=parent[temp]
			if temp==start:
				return path[::-1]   

		#END YOUR CODE HERE

	def dfs_paths(self, start, goal):
		'''
		Generate and return any path from start to goal using depth-first search
		Input : start node, goal node
		Output : list of nodes from to be traversed to reach from start to goal(the first node in this list will be the start node and the last node will be the goal node)
		'''
		#BEGIN YOUR CODE HERE
		visited = [0 for _ in range(len(self.graph.keys()))]
		parent={}
		stack=[]
		stack.append(start)
		while(len(stack)):
			s=stack.pop()
			visited[s]=1
			for child in self.graph[s]:
				if not visited[child]:
					parent[child]=s
					stack.append(child)
		temp=goal
		path=[goal]
		for i in range(len(self.graph.keys())):
			path.append(parent[temp])
			temp=parent[temp]
			if temp==start:
				return path[::-1]
	    #END YOUR CODE HERE
