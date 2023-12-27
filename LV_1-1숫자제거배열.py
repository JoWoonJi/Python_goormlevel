
#practice
def eatnumber(n,k,num_list):
	n = len(num_list)
	str_k = str(k)
	atenum_count = 0
	
	for temp_num in num_list:
		if str_k not in str(temp_num): 
			atenum_count += 1
	return atenum_count

#입력예제
n,k = map(int,input().split())
num_list = list(map(int,input().split()))

result = eatnumber(n,k,num_list)
print(result)
		
''' source 
def solution(n, k, numbers):
    k_str = str(k)
    included_count = 0
 
    for num in numbers:
        if k_str not in str(num):
            included_count += 1
    return included_count
 
# 입력 예제
n,k = map(int,input().split())
a = list(map(int,input().split()))
 
result = solution(n, k, a)
print(result)
'''