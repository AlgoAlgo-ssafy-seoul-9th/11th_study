def solution(input_string):
    alpha_dict = {}
    ans = []
    length = len(input_string)
    idx = 0
    while True:
        if idx == length:
            break
        text = input_string[idx]
        temp = idx+1
        while True:
            if temp < length:
                if input_string[temp] == text:
                    temp += 1
                else:
                    break
            else:
                break
        idx = temp-1
        
        if text in alpha_dict.keys():
            if text not in ans:
                ans.append(text)
        else:
            alpha_dict[text] = 0
        idx += 1
    ans = sorted(ans)
    if ans:
        answer = ''.join(ans)
    else:
        answer = 'N'
    return answer