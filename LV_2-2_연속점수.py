def max_sum_straight(s):
    max_sum = 0
    current_sum = 0

    for i in range(len(s)):
        # 현재 숫자와 이전 숫자가 연속되지 않은 경우
        if i > 0 and s[i] != s[i - 1] + 1:
            current_sum = 0

        current_sum += s[i]
        max_sum = max(max_sum, current_sum)

    return max_sum

n = int(input())
s = list(map(int, input().split()))

highest = max(s)
a = max_sum_straight(s)

print(max(a, highest))


''' 뭐가 잘못됐는지 안됨. 결국 max함수 사용해서 해결
n = int(input())
s = list(map(int,input().split()))

highest = 0
for i in s:
	if highest < i:
			highest = i


def max_sum_straight(s):
  
  max_sum = 0
  current_sum = 0
  start = 0

  for i in range(len(s)):
    current_sum += s[i]

    # 현재 숫자와 이전 숫자가 연속되지 않을 경우
    if i > 0 and s[i] != s[i - 1] + 1:
      # 현재 합이 최대 합보다 크면 최대 합을 갱신
      if current_sum > max_sum:
        max_sum = current_sum

      # 새로운 연속된 숫자 구간 시작
      start = i
      current_sum = s[i]

  # 마지막 연속된 숫자 구간 처리
  if current_sum > max_sum:
    max_sum = current_sum

  return max_sum
a = max_sum_straight(s)

if a < highest:
     print(highest)
else:
     print(a)
'''
