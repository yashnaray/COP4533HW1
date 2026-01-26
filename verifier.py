from typing import List


def gsverify(matched_pairs:List[List[int]], h_prefs:List[List[int]], s_prefs:List[List[int]])->str:
    n = len(matched_pairs)
    
    hospitals = [pair[0] for pair in matched_pairs]
    students = [pair[1] for pair in matched_pairs]
    
    if len(set(hospitals)) != n or len(set(students)) != n:
        return "INVALID: Not a one-to-one matching"
    
    if set(hospitals) != set(range(1, n+1)) or set(students) != set(range(1, n+1)):
        return "INVALID: Missing hospitals or students"
    
    h_to_s = {pair[0]: pair[1] for pair in matched_pairs}
    s_to_h = {pair[1]: pair[0] for pair in matched_pairs}
    
    h_rank = [[0]*n for _ in range(n)]
    s_rank = [[0]*n for _ in range(n)]
    
    for h in range(n):
        for rank, s in enumerate(h_prefs[h]):
            h_rank[h][s-1] = rank
    
    for s in range(n):
        for rank, h in enumerate(s_prefs[s]):
            s_rank[s][h-1] = rank
    
    for h in range(1, n+1):
        for s in range(1, n+1):
            current_s = h_to_s[h]
            current_h = s_to_h[s]
            
            if h_rank[h-1][s-1] < h_rank[h-1][current_s-1] and s_rank[s-1][h-1] < s_rank[s-1][current_h-1]:
                return f"UNSTABLE: Blocking pair ({h}, {s})"
    
    return "VALID STABLE"