from collections import deque

def solution(people, limit):
    deq_p = deque(sorted(people,reverse=True))
    cnt=0
    
    
    while len(deq_p)>1:
        if(deq_p[0]+deq_p[-1])<=limit:
            deq_p.popleft()
            deq_p.pop()
            cnt+=1
        else:
            deq_p.popleft()
            cnt+=1
    
    cnt+=len(deq_p)
    return cnt