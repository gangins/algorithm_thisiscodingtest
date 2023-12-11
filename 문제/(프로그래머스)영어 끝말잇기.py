def solution(n, words):
    answered = set()  # 더 빠른 조회를 위해 세트 사용
    for i, word in enumerate(words):
        # 단어가 반복되었거나 마지막 글자 규칙을 따르지 않는 경우 검사
        if word in answered or (i > 0 and words[i - 1][-1] != word[0]):
            return [(i % n) + 1, (i // n) + 1]
        answered.add(word)

    return [0, 0]  # 탈락자가 없는 경우
