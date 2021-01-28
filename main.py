

def solution(s): 
  a=sorted(s) 
  for x in range(len(a)-1):
    for y in range(x+1,len(a)):
      if a[x]<a[y]:
        temp = a[x]
        a[x] = a[y]
        a[y] = temp   

  answer = ''
  for x in range(len(a)):
    answer +=a[x]
  return answer


print(solution("Zbcdefg"))
