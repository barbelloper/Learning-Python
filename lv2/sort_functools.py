import functools

def comparator(a,b):
    
    if int(a+b)>int(b+a):
        return 1
    elif int(a+b)<int(b+a):
        return -1
    else:
        return 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer