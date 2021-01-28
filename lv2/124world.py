def solution(n):
  #124나라의 숫자 규칙 1 : 4진법 숫자에서 일정한 수를 더한 숫자이다.
    cnt=0
    for x in range(2,n): #2부터 n까지의 수를 3으로 나누었을 때 나머지가 1인 숫자의 개수만큼 +1씩 커진다.
      if x%3 ==1:       #그 커진 수를 4진법으로 변환한 후 0은 1로 3은 4로 변환하면 124나라 숫자가 완성.
        cnt+=1
    n=n+cnt #매개변수로 받은 10진법 수를 4진법으로 고쳤을때 10진법으로 변환
    arr=[]  #124나라의 각자리 숫자를 받을 리스트 
    OTF_world=0 #124나라의 각자리 숫자
    answer=0
    while True:
        OTF_world=n%4
        if(n%4==3):
            OTF_world=4                 
        if(n%4==0):
            OTF_world=1                  #4진법 변환
        arr.append(OTF_world)
        if((n//4)<1):
          break
        n=n//4
       
    arr_len=len(arr)
    
    for x in range(arr_len):       #리스트를 정수형으로 변환
        answer+=arr[x]*10**x  
    
    answer=str(answer)    #정수를 문자열로 변환
    return answer


print(solution(9825))