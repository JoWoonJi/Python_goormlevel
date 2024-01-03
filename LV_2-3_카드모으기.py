def min_cards_to_win_game(N, M, cards):
    # 각 카드 종류의 개수를 저장하는 배열 초기화
    card_count = [0] * (N + 1)
    
    # 현재까지 받은 카드의 종류를 저장하는 집합 초기화
    unique_cards = set()
    
    # 전체 카드의 종류를 저장하는 집합 초기화
    total_unique_cards = set(range(1, N + 1))
    
    # 최소 카드 개수를 무한대로 초기화
    min_cards = float('inf')
    
    # 현재까지 받은 카드의 총 개수 초기화
    received_cards = 0  

    # 카드를 하나씩 받으며 처리
    for i in range(M):
        # 현재 받은 카드가 처음으로 받는 종류라면
        if card_count[cards[i]] == 0:
            received_cards += 1  # 받은 카드의 종류 수 증가
            
        card_count[cards[i]] += 1  # 현재 받은 카드 종류의 개수 증가

        # 현재까지 받은 모든 종류의 카드를 다 모았을 경우
        while received_cards == N:
            min_cards = min(min_cards, i + 1)  # 최소 카드 개수 갱신
            
            # 가장 처음에 받은 카드를 하나 뺀다
            card_count[cards[i - received_cards + 1]] -= 1
            
            # 뺀 카드가 더 이상 남아있지 않다면 종류 수를 감소
            if card_count[cards[i - received_cards + 1]] == 0:
                received_cards -= 1

    # 최소 카드 개수가 갱신되지 않았으면 모든 종류의 카드를 모을 수 없다는 의미이므로 -1 출력
    if min_cards == float('inf'):
        return -1
    else:
        return min_cards

# 입력 받기
N, M = map(int, input().split())
cards = [int(input()) for _ in range(M)]

# 결과 출력
result = min_cards_to_win_game(N, M, cards)
print(result)

# user_input = input().split(' ')
# N = int(user_input[0])
# M = int(user_input[1])
# ar = [0 for i in range(1,N+1)]
# tf = True
# count = 0
# s = -1
# for i in range(1,M+1):
# 	k = int(input()) -1
# 	if ar[k] == 0:
# 		ar[k] = 1
# 		count = count +1
# 	if count == M:
# 		s = M
# 		break
# 	if count == N and tf:
# 		s = i
# 		tf = False
	
	
# print(s)