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