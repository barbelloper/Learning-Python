def multpoly(A,B) :
  answer = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

  for x in range(len(A)):
    for y in range(len(B[0])):
      for z in range(len(A[0])):
         answer[x][y] += (A[x][z]*B[z][y])
  
  
  return answer

print(multpoly([[1, 4], [3, 2], [4, 1]],[[3,3],[3,3]]))
