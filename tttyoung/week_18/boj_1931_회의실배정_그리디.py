#배정받은 회의시간 리스트를 참고하여 가능한 최대 회의 수 구하기

def max_meeting(N, meetinglist):
    #starttime = -1
    endtime = -1
    count = 0
    for meeting in meetinglist:#문제에서는 회의가 아예 중복인경우 각각 계산해주는듯듯
        if meeting[0] >= endtime: #and meeting[1] != starttime 이거는 왜 틀린거지? 4 (0 0) (0 0) (0 1) (1 1)은 3 나와야하는거 아님?
            count+=1
            endtime = meeting[1]
            #starttime = meeting[0]
    return count
    
N = int(input())
meetinglist = [list(map(int, input().split())) for _ in range(N)]
meetinglist.sort(key=lambda x: (x[1], x[0])) #입력받은 회의시간들을 1순위:끝나는시간, 2순위:시작시간으로 정렬함
#2순위까지 정렬해야 (3 3) (4 4) (1 4) (3 4) 이런 경우 (3 3) 다음에 (3 4)가 나옴. 정렬 안하면 (4 4) 나옴옴
print(max_meeting(N, meetinglist))
