def solution(array, commands):
    n = len(commands)
    answer = []
    for i in range(n):
        command = commands[i]

        lst = array[command[0] - 1:command[1]]
        lst = sorted(lst)

        answer.append(lst[command[2] - 1])

    return answer