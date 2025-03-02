import numpy as np

def pagerank(G, beta=0.85, tol=1.0e-6, max_iter=100):
    """
    Computes the PageRank for a given adjacency matrix G.
    
    Parameters:
    G: numpy array - Adjacency matrix representing the graph
    beta: float - Damping factor (default is 0.85)
    tol: float - Convergence tolerance (default is 1.0e-6)
    max_iter: int - Maximum number of iterations (default is 100)
    
    Returns:
    numpy array - PageRank scores for each page
    """
    n = len(G)
    
    # Convert adjacency matrix to a stochastic matrix
    M = np.zeros((n, n))
    for i in range(n):
        row_sum = np.sum(G[i])
        if row_sum == 0:  # Handling dangling nodes (pages with no outlinks)
            M[i] = np.ones(n) / n
        else:
            M[i] = G[i] / row_sum  # Normalize row to make it stochastic
    
    # Initialize rank vector with equal probability
    R = np.ones(n) / n
    
    # Teleportation matrix (used to handle rank sinks)
    E = np.ones((n, n)) / n
    
    # Compute transition probability matrix with damping factor
    A = beta * M + (1 - beta) * E
    
    # Iteratively compute PageRank
    for _ in range(max_iter):
        new_R = A @ R  # Matrix-vector multiplication
        if np.linalg.norm(new_R - R, ord=1) < tol:  # Convergence check
            break
        R = new_R
    
    return np.round(R, 5)  # Round results for better readability

# Example adjacency matrix (3 pages linking to each other)
G = np.array([
    [0, 1, 1],
    [0, 1, 0],
    [1, 0, 1]
])

# Compute PageRank
page_ranks = pagerank(G)
print("Final PageRank Scores:", page_ranks)
