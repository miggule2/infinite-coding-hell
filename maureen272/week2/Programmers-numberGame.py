def solution(A, B):
    A.sort()
    B.sort()
    score = 0
    i = 0 
    
    for a in A:
        while i < len(B) and B[i] <= a:
            i += 1
        if i < len(B):
            score += 1
            i += 1
            
    return score
