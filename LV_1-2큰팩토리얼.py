#practice

def factorial_mod(n,mod):
	result=1
	for i in range (1,n+1):
			result = result * i
	return result % mod

try:
 num = int(input())
 mod = 1000000007
 result = factorial_mod(num,mod)
 print(result)
	
except ValueError:
 print("올바른 정수를 입력해 주세요")



''' source
def factorial_mod(n, mod):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % mod
    return result
 
try:
    num = int(input())
    mod = 1000000007
    result = factorial_mod(num, mod)
    print(result)
except ValueError:
    print("올바른 정수를 입력해주세요.")
'''