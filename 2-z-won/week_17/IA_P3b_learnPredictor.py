import random
import collections
import math
import sys
from collections import Counter
from util import *

def learnPredictor(trainExamples, testExamples, featureExtractor, numIters, eta):
    '''
    Given |trainExamples| and |testExamples| (each one is a list of (x,y)
    pairs), a |featureExtractor| to apply to x, and the number of iterations to
    train |numIters|, the step size |eta|, return the weight vector (sparse
    feature vector) learned.

    You should implement stochastic gradient descent.

    Note: only use the trainExamples for training!
    You should call evaluatePredictor() on both trainExamples and testExamples
    to see how you're doing as you learn after each iteration.
    '''
    weights = {}  # feature => weight
    # BEGIN_YOUR_CODE (our solution is 12 lines of code, but don't worry if you deviate from this)
    for iter in range(numIters):
        for x, y in trainExamples:
            phi = featureExtractor(x)
            margin = y * dotProduct(weights, phi)
            if margin < 1:
                increment(weights, eta * y, phi)

        def predictor(x):
                return 1 if dotProduct(weights, featureExtractor(x)) >= 0 else -1
        
        trainErr = evaluatePredictor(trainExamples, predictor)
        testErr  = evaluatePredictor(testExamples, predictor)
        print(f"iter {iter}: train error = {trainErr:.4f}, test error = {testErr:.4f}")
    # END_YOUR_CODE
    return weights

############################################################
# Problem 3d: character features

def extractCharacterFeatures(n):
    '''
    Return a function that takes a string |x| and returns a sparse feature
    vector consisting of all n-grams of |x| without spaces.
    EXAMPLE: (n = 3) "I like tacos" --> {'Ili': 1, 'lik': 1, 'ike': 1, ...
    You may assume that n >= 1.
    '''
    def extract(x):
        # BEGIN_YOUR_CODE (our solution is 6 lines of code, but don't worry if you deviate from this)
        s = ''.join(x.split())
        features = {}
        for i in range(len(s) - n + 1):
            ngram = s[i:i+n]
            features[ngram] = features.get(ngram, 0) + 1
        return features
        # END_YOUR_CODE 
    return extract

############################################################
# Problem 4: k-means
############################################################


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
