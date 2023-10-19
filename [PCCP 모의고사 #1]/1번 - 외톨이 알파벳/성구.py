from collections import defaultdict

def solution(input_string):
    # 중복 제거하기 위해 set
    answer = set([])
    # 이전 값과 비교하기 위해 0패딩
    input_string= f'0{input_string}'
    # 개수 비교용 dictionary
    alpha = defaultdict(int)
    # 반복으로 떠돌이 문자 찾기
    for i in range(1, len(input_string)):
        # 이전 문자와 같으면 체크 안함
        if input_string[i] != input_string[i-1]:
            alpha[input_string[i]] += 1
        # 만약 2이상이면 추가
            if alpha[input_string[i]] >= 2:
                answer.add(input_string[i])
    # answer가 있다면 순서대로 출력 아니면 N
    return ''.join(sorted(answer)) if answer else 'N'