# len 함수 사용하지 않고 직접 만들어서 수학적으로
def get_length(num):
    length=0

    if num == 0:
        return 1
    is_negative=False
    if num < 0:
        is_negative=True
        length+=1
        num = abs(num)
        
    while num!=0:
        num //= 10
        length +=1
    return length
    
num = int(input())
numlength = get_length(num)
print(numlength)

''' 가장 간단하게. len내장함수 사용
n = input()
print(len(n))
'''