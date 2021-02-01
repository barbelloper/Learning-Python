def solution(n,words):
    
    answer=[0,0]
    for x in range(1,len(words)):
            if words[x][0]!=words[x-1][-1] or words[x] in words[:x]:
                answer = [(x%n)+1,((x)//n)+1]
                return answer
    return answer