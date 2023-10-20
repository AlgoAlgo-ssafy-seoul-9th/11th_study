# 최댓값 저장
maxV = 0

# 전체 순회
def dfs(N, M, ability, j, val, stack):
    global maxV
    # 만약 모든 종목을 탐색했다면
    if j == M:
        # 최대 체크
        maxV = max(maxV, val)
        return
    
    # 학생 순회
    for x in range(N):
        # 출전한 종목이 없다면
        if not stack[x]:
            # 출전해보고
            stack[x] = 1
            # 점수 확인
            dfs(N, M, ability, j+1, val + ability[x][j], stack)
            # 출전취소
            stack[x] = 0
    return
    

def solution(ability):
    global maxV
    # 길이를 미리 저장
    N , M = len(ability), len(ability[0])
    # visited
    stack = [0] * N
    
    dfs(N, M, ability, 0, 0, stack)
    return maxV