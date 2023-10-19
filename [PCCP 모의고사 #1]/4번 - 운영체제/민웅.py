import heapq
from collections import deque


def solution(program):
    answer = [0]*11
    # [점수, 호출시간, 실행시간]

    program.sort(key=lambda x: [x[1], x[0]])

    q = deque(program)
    t = 0
    hq = []
    while True:
        # 프로그램도 다 호출했고, 실행도 끝났으면 종료
        if not hq and not q:
            break
        # 이전 프로그램 실행종료시간 전까지 호출된 프로그램 다 넣기(우선순위 기준으로 정렬하고 heapq로)
        while q and q[0][1] <= t:
            p = q.popleft()
            heapq.heappush(hq, (p[0], p))

        if hq:
            # 우선순위 제일 높은거로 실행하고 종료
            p = heapq.heappop(hq)[1]
            # 시간 계산
            wait_time = t - p[1]
            answer[p[0]] += wait_time
            t += p[2]
        else:
            t = q[0][1]
            
    answer[0] = t
    return answer
