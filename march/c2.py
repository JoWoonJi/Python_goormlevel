import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# index 처리를 위해서 N + 1 까지의 배열 선언
menuList = [0 for _ in range(N+1)]

# 메뉴의 번호와 주문 개수를 menuList 에 추가
for i in range(M):
    menuNum, orderCount = map(int, input().split())
    menuList[menuNum] += orderCount

# 가장 많이 판매가 된 메뉴의 번호 찾기
ans = 0
for idx in range(N):
    if menuList[ans] <= menuList[idx]:
        ans = idx

print(ans)