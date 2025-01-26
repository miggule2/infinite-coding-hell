def print_all_friends(g, start):
    qu = []
    done = set()

    qu.append(start) #앞으로 처리해야 할 사람들일 큐에 저장
    done.add(start) #이미 큐에 추가한 사람들을 set에 저장(중복방지)

    while qu: #큐에 사람이 남아있는동안
        p = qu.pop(0) #큐에서 처리대상 한명을 꺼내
        print(p)
        for x in g[p]: #그 처리대상과 연결되어있는 인물들을 for문으로 돌려서 
            if x not in done: #set에 없으면(아직 큐에 추가된 적 없는 사람) 새로 추가
                qu.append(x)
                done.add(x)

fr_info = {
        'Summer' :[ 'John', 'Justin', 'Mike'],
        'John' :['Summer', 'Justin'],
        'Justin' : ['John', 'Summer', 'Mike', 'May'], 
        'Mike' :['Summer', 'Justin'], 
        'May' : ['Justin', 'Kim'], 
        'Kim' :['May'], 
        'Tom' :['Jerry'], 
        'Jerry' : ['Tom']
    }

print_all_friends(fr_info, 'Summer')
print()
print_all_friends(fr_info, 'Jerry')

