from collections import defaultdict


def solution(genres, plays):
    answer = []
    songs_genre = defaultdict(list)

    # 1. 장르별로 곡 정보 저장
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        songs_genre[genre].append((idx, play))

    # 2. 장르별 총 재생수로 정렬
    genre_order = sorted(songs_genre.items(), key=lambda x: sum(song[1] for song in x[1]), reverse=True)

    # 3. 각 장르별로 재생수, 인덱스 기준 정렬 후 최대 2곡 선택
    for genre, songs in genre_order:
        top_songs = sorted(songs, key=lambda x: (-x[1], x[0]))[:2]
        answer.extend([idx for idx, _ in top_songs])

    return answer