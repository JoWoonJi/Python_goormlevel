def m_multiple(n,m):
	for i in range(n):
		if a_list[i] % m != 0:
			a_list[i] *= m
	return a_list

n,m = map(int,input().split())
a_list = list(map(int,input().split()))

result = m_multiple(n,m)

print(*result)