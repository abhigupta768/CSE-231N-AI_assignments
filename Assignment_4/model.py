"""
model.py

This file implements the Logistic Regression model for classification.
"""

import numpy as np

class Kmeans(object):

    def __init__(self, dist = 'euc'):
        """
        Initialise the model. Here, we only initialise the weights as 'None',
        as the input size of the model will become apparent only when some
        training samples will be given to us.

        @add_bias: Whether to add bias.
        """

        # Initialise model parameters placeholders. Don't need another placeholder
        # for bias, as it can be incorporated in the weights matrix by adding
        # another feature in the input vector whose value is always 1.
        self.n_clusters = None
        self.n_data_points = None
        self.n_dimensions = None
        self.n_iterations = None

        self.centers = None
        self.labels = None
        self.dist = dist

    def distance(self, a, b):
        if(self.dist == 'euc'):
            return self.euc(a,b)

    def euc(self,a,b):
        ''' Input - @a, @b are two vectors
            Output - return a single value which is the difference of @a and @b
        '''
        ''' YOUR CODE HERE'''
        Output = np.linalg.norm(a-b)
        return Output
        ''' YOUR CODE ENDS'''

    def cluster(self, X, k = 1, n_iter = 10, debug = True):
        self.n_clusters = k
        self.n_iterations = n_iter
        self.n_data_points = X.shape[0]
        self.n_dimensions = X.shape[1]

        # INITIALIZATION
        #self.centers = np.random.randn(self.n_clusters,self.n_dimensions)
        
        '''
        Pick @k cluster centers randomly from the data points (@X) and store the sampled points in a variable called @self.centers
        '''
        ''' YOUR CODE HERE'''
        self.centers = X[np.random.choice(X.shape[0], self.n_clusters, replace = False), :]
        ''' YOUR CODE ENDS'''

        self.labels = np.zeros(self.n_data_points)
        '''
            Update the cluster centers now.
        '''
        ''' YOUR CODE HERE'''
        for _ in range(self.n_iterations):
        # Loop here.
            for i,x in enumerate(X):
                min_dist = 1e12
                for j,center in enumerate(self.centers):
                    dist = self.euc(x,center)
                    #print(i,j,dist)
                    if dist < min_dist:
                        #print(i,j,dist)
                        min_dist = dist
                        self.labels[i] = j
            # Allocate label to each document
            for i,center in enumerate(self.centers):
                self.centers[i][:] = np.mean(X[np.unique(np.where(self.labels == i)[0]), :], axis = 0)
            #print(self.centers)
            # Find new cluster centers
        
        ''' YOUR CODE ENDS'''

        return self.labels
