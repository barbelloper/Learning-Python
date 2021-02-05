def solution(citations):
    answer = 0
    leng = len(citations)
    citations.sort(reverse=True)
    print(citations)
    
    for x in range(leng):
        if citations[x]<x+1:
            answer=x
            break
        else:
            answer = leng
               
    return answer