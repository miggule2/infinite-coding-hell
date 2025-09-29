def sparseVectorDotProduct(v1, v2):
    """
    Given two sparse vectors |v1| and |v2|, each represented as collection.defaultdict(float), return
    their dot product.
    You might find it useful to use sum() and a list comprehension.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    from collections import defaultdict
    v1 = defaultdict(float, v1)
    v2 = defaultdict(float, v2)
    return sum(v1[k] * v2[k] for k in v1)
    # END_YOUR_CODE