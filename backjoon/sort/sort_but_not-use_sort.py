import sys
N = int(input())
check_list = [0]*10001
for i in range(N): 
  input_num = int(sys.stdin.readline()) 
  check_list[input_num] +=1

for i in range(10001): 
  if check_list[i] != 0:
    sys.stdout.write((str(i)+'\n')*check_list[i])

