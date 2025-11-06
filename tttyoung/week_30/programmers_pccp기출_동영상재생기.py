def solution(video_len, pos, op_start, op_end, commands):
    def to_sec(time): #문자열 시간을 int형 초 단위로 변형
        m, s = map(int, time.split(":"))
        return 60*m + s
    #모든 문자열 시간 변환
    video_len = to_sec(video_len)
    pos = to_sec(pos)
    op_start = to_sec(op_start)
    op_end = to_sec(op_end)
    
    for i in commands:
        if op_start<=pos<=op_end: #오프닝시간
            pos = op_end
        if i == "next":
            pos = min(video_len, pos+10) #영상종료 10초이내라면 next일때 영상종료시점으로 이동
        elif i == "prev":
            pos = max(0, pos-10) #영상시작 10초이내라면 prev일때 영상시작시점으로 이동
    if op_start<=pos<=op_end:
            pos = op_end
    answer = f'{(pos//60):02}:{(pos%60):02}' #2자리 int로 출력형태 맞추기
    return answer