def solution(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:  # 스택의 최상단 요소와 현재 문자가 같다면 스택부분에서 이미오류
            stack.pop()  # 스택의 최상단 요소 제거
        else:
            stack.append(char)  # 스택에 현재 문자 추가

    return 1 if not stack else 0  