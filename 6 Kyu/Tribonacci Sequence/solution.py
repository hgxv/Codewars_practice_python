def tribonacci(signature, n):
    if n == 0:
        return []
    
    result = []
    
    while len(result) < n:
        if len(signature) == 0:
            result.append(sum(result[-3:]))
        else:
            result.append(signature.pop(0))
    
    return result