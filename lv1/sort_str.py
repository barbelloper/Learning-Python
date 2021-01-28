def solution(s): 
  a=sorted(s,reverse=True) 
  answer = ''
  for x in range(len(a)):
    answer +=a[x]
  return answer


print(solution("Zbcdefg"))
