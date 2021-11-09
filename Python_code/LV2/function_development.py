def solution(progresses, speeds):
    answer = []
    _progresses = progresses
    _speeds = speeds
    cnt = 0
    time = 0

    while len(_progresses) > 0:
        if _progresses[0] + (_speeds[0] * time) >= 100: # 100 보다 크면 pop(0) , FIFO queue
            cnt += 1
            _progresses.pop(0)
            _speeds.pop(0)
        else :
            time += 1
            if cnt >= 1:                                # cnt >= 이면 append 해주고 cnt 초기화
                answer.append(cnt)
                cnt = 0
    answer.append(cnt) # 마지막 담고 있는 cnt 추가

    return answer