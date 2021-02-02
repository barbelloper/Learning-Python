from itertools import combinations

def solution(people, limit):
    cnt=0
    com=list(combinations(people,2))
    s_com=sorted(com,key=lambda x: sum(x),reverse=True)
    p=people
            
    for x in range(len(s_com)):
        if sum(s_com[x])<=limit:
                if (s_com[x][0] in p) and (s_com[x][1] in p):
                    if(s_com[x][0]==s_com[x][1]):
                        if (p.count(s_com[x][0])==1):                                
                            continue
                        else:
                            p.remove(s_com[x][0])                  
                            p.remove(s_com[x][1])
                            cnt+=1                    
                    else:
                        p.remove(s_com[x][0])                  
                        p.remove(s_com[x][1])
                        cnt+=1 
        else:
            continue
    cnt+=len(p)
                       
    return cnt