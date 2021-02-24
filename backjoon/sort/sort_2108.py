import sys
import math

def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)
N = int(input())

num_list=[0]*N
answer=[]
sum=0
dict_count=[]


for x in range(N):
  num_list[x]=int(sys.stdin.readline())
  sum+=num_list[x]

num_list.sort()
answer.append(normal_round(sum/N))  #산술평균
answer.append(num_list[((N+1)//2)-1]) #중간값

num_list_dict = dict.fromkeys(num_list,0)

for i in range(N):
  num_list_dict.update({num_list[i]:num_list_dict.get(num_list[i])+1})  #빈도수 구하기

sorted_dict = sorted(num_list_dict,key=lambda k: num_list_dict[k],reverse=True) #빈도수로 딕셔너리 정렬
for i in sorted_dict:
  if not num_list_dict.get(i)==num_list_dict.get(sorted_dict[0]):
    del num_list_dict[i]

answer_sorted_dict = sorted(num_list_dict.keys())

if not len(answer_sorted_dict)==1:   #최빈값 구하기
  answer.append(answer_sorted_dict[1])
else:
  answer.append(answer_sorted_dict[0])

answer.append(num_list[N-1]-num_list[0])  #범위 

for i in answer:
  print(i)






