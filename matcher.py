from typing import List
from time import time

def gsmatch(n, h_prefs, s_prefs):
    s_rank = [[0]*n for _ in range(n)]
    
    for s in range(n):
        for rank, h in enumerate(s_prefs[s]):
            s_rank[s][h-1] = rank
    
    h_match = [-1] * n
    s_match = [-1] * n
    h_next = [0] * n
    
    free_hospitals = list(range(n))
    
    while free_hospitals:
        h = free_hospitals.pop(0)
        s = h_prefs[h][h_next[h]] - 1
        h_next[h] += 1
        
        if s_match[s] == -1:
            h_match[h] = s
            s_match[s] = h
        else:
            current_h = s_match[s]
            if s_rank[s][h] < s_rank[s][current_h]:
                h_match[h] = s
                s_match[s] = h
                h_match[current_h] = -1
                free_hospitals.append(current_h)
            else:
                free_hospitals.append(h)
    
    return [[i+1, h_match[i]+1] for i in range(n)]
