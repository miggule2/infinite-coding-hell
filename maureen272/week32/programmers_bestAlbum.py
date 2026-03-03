from collections import defaultdict

def solution(genres, plays):
    # 장르별 총 재생수, 장르별 노래 목록(재생수, 고유번호)
    total_by_genre = defaultdict(int)
    songs_by_genre = defaultdict(list)

    for i, (g, p) in enumerate(zip(genres, plays)):
        total_by_genre[g] += p
        # 정렬을 편하게 하기 위해서 (-재생수, 고유번호)로 저장 => 내림차순 정렬
        songs_by_genre[g].append((-p, i))

    # 장르를 총 재생수 내림차순으로 정렬
    genre_order = sorted(total_by_genre.keys(), key=lambda g: -total_by_genre[g])

    # 각 장르에서 최대 2곡 선택
    answer = []
    for g in genre_order:
        top_songs = sorted(songs_by_genre[g])[:2]
        answer.extend(idx for _, idx in top_songs)

    return answer
