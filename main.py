def solution(s):
    s_list=[]
    for i in s:
        s_list.append(i)
    s_list[0]=s_list[0].upper()
    for j in range(1,len(s_list)):    
        if s_list[j].isupper()==True and s_list[j-1]==' ':
            s_list[j]=s_list[j].lower()
        elif s_list[j].islower()==True and s_list[j-1]==' ':
            s_list[j]=s_list[j].upper()
        else:
            s_list[j]=s_list[j].lower()

    for x in range(1,len(s_list)):
        s_list[0] +=s_list[x]

    answer = s_list[0]
    return answer

print(solution('ADV deadf ADF advE'))