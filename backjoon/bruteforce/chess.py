n,m = map(int,input().split())
graph=[]
for i in range(n):
  graph.append(list(input()))


def answer(graph):
  cnt1=0
  cnt2=0
  chess1=['B','W']
  chess2=['W','B']
  cnt=[]
  
  for k in range(0,n-8+1):
    for l in range(0,m-8+1):
      for i in range(k,k+8):
        for j in range(l,l+8):
          if not graph[i][j]==chess1[j%2-i%2]:
            cnt1+=1
          if not graph[i][j]==chess2[j%2-i%2]:
            cnt2+=1   
                               
      cnt.append(cnt1)
      cnt.append(cnt2)
      cnt1=0
      cnt2=0

  return min(cnt)

print(answer(graph))



