import random
import collections
import math
import sys
from collections import Counter
from util import *

def kmeans(examples, K, maxIters):
    '''
    examples: list of examples, each example is a string-to-double dict representing a sparse vector.
    K: number of desired clusters. Assume that 0 < K <= |examples|.
    maxIters: maximum number of iterations to run for (you should terminate early if the algorithm converges).
    Return: (length K list of cluster centroids,
            list of assignments, (i.e. if examples[i] belongs to centers[j], then assignments[i] = j)
            final reconstruction loss)
    '''
    # BEGIN_YOUR_CODE (our solution is 32 lines of code, but don't worry if you deviate from this)
    N = len(examples)
    assert 0 < K <= N
    exampleNorms = [dotProduct(x, x) for x in examples]
    indices = random.sample(range(N), K)
    centers = [examples[i].copy() for i in indices]

    assignments = [0] * N

    for _ in range(maxIters):
        changed = False
        centerNorms = [dotProduct(c, c) for c in centers]

        for i, x in enumerate(examples):
            xNorm = exampleNorms[i]
            best_k = None
            best_dist = None
            for k, c in enumerate(centers):
                d = xNorm - 2 * dotProduct(x, c) + centerNorms[k]
                if best_dist is None or d < best_dist:
                    best_dist = d
                    best_k = k
            if assignments[i] != best_k:
                assignments[i] = best_k
                changed = True

        newCenters = [{} for _ in range(K)]
        counts = [0] * K
        for i, x in enumerate(examples):
            k = assignments[i]
            increment(newCenters[k], 1.0, x)
            counts[k] += 1

        for k in range(K):
            if counts[k] == 0:
                newCenters[k] = centers[k]
            else:
                inv = 1.0 / counts[k]
                for f in list(newCenters[k].keys()):
                    newCenters[k][f] *= inv

        centers = newCenters
        if not changed:
            break
    centerNorms = [dotProduct(c, c) for c in centers]
    totalCost = 0.0
    for i, x in enumerate(examples):
        k = assignments[i]
        xNorm = exampleNorms[i]
        d = xNorm - 2 * dotProduct(x, centers[k]) + centerNorms[k]
        totalCost += d

    return centers, assignments, totalCost
    # END_YOUR_CODE
