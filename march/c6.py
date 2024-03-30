import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
obstacle = [0] + list(map(int, input().split()))
X, Y = map(int, input().split())
command = list(input())

for i in command:
    if i == "L":
        X -= 1
    elif i == "R":
        X += 1
    elif i == "D":
        Y -= 1
    elif i == "U":
        Y += 1
    if Y < obstacle[X]:
        print("CRASHED")
        exit()
    elif L < Y or X < 1 or N < X:
        print("OUT")
        exit()
print(X, Y)

# 문제 내용 정리
# 문제의 내용이 복잡하지만 정리하면 간단합니다.

# 우선 길이가 N인 배열이 있습니다. 이 배열에 너비는 1이고, 높이가 H인 장애물이 각 칸에 있다고 합니다.

# 이런 배열에 비행기를 띄우는 게임을 진행합니다. 비행기는 L, R, U, D 4개의 명령을 수행할 수 있고, 각각 현재 위치에서 왼쪽, 오른쪽, 위, 아래로 이동합니다. 이때 비행기가 주어진 모든 입력을 수행할 수 있는지 확인하는 문제입니다.

# 이때, 항상 비행기가 날 수 있는 있지는 않다고 합니다. 크게 2가지 경우가 있는데, 하나는 비행 가능 구역을 이탈한 경우(OUT)와 비행기가 장애물에 부딪친 경우(CRAHSED) 입니다.

# M개의 입력과 현재 비행기의 위치가 주어졌을 때, 비행기가 잘 비행할 수 있을지 확인하는 문제입니다.


# 문제 풀이
# 비행기 게임 문제의 본질은 배열에서 이동하는 것이 주된 요구 사항입니다. 현재 위치인 X, Y에서 4가지 명령을 수행하는 것을 구현하면 됩니다. 명령어에 따라서, X, Y의 좌표를 이동하면 어렵지 않게 구현할 수 있습니다.

# 명령을 구현하는 방법은 Switch ~ Case를 사용해도 되고, 경우가 적기 때문에 조건문을 사용해도 되지만 중요한 것은 방향에 따라서 X, Y 좌표 둘 다 이동하는 것이 아닌, L이나 R은 X의 좌표를, U나 D는 Y의 좌표를 1만큼 위치를 수정하기만 하면 됩니다.

# 또 다른 문제의 핵심은 비행 중에 게임이 종료되는 경우입니다. 하나는 장애물에 부딪친 경우이고, 다른 하나는 비행 가능 구역으로 이탈하는 것입니다.

# 비행기의 Y좌표가 L보다 높거나, X 좌표가 N보다 크거나 1보다 작다면(L < Y or X < 1 or N < X), 비행 가능 구역을 이탈한 것이고, 만약에 현재 높이가 장애물의 높이보다 낮다면(Y < obstacle[X]) 장애물과 부딪치고 비행이 종료됩니다. 매 비행기가 이동할 때 마다 이 위치를 검사하여 계속 비행이 가능한 지 확인해야 합니다.


# Comment.
# 비행기 게임 문제처럼 문제의 요지는 간단하지만, 문제 내용이 긴 경우가 있습니다. 이런 문제의 경우에는 문제의 요구 사항을 정확히 파악하고 정리해야 합니다. 문제를 읽으면서 실제 요구 사항이 무엇이고, 고민하지 않아도 되는 요구 사항은 무엇인지 문제를 읽지 않아도 이해할 수 있을 정도로 빠르게 정리해야 합니다.

# 이런 시뮬레이션 문제는 알고리즘 자체는 단순하지만 코드를 길게 작성하거나 문제를 여러 번 읽음으로써 시간을 많이 사용하게 되기 때문에 요구 사항을 간결하게 정리하는 연습이 반드시 필요합니다.