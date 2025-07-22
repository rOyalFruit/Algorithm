def parse_file_name(file):
    head = ""
    number = ""
    
    # HEAD 추출
    i = 0
    while file[i].isalpha() or file[i] in [" ", ".", "-"]:
        head += file[i]
        i += 1
    
    # NUMBER 추출
    while i < len(file) and file[i].isdigit():
        number += file[i]
        i += 1
    
    return head.lower(), int(number)


def solution(files):
    # 파일명을 파싱하고 정렬 키와 함께 저장
    parsed_files = []
    for idx, file in enumerate(files):
        head, number = parse_file_name(file)
        parsed_files.append((head, number, idx, file))
    
    # HEAD(대소문자 무시) -> NUMBER(숫자값) -> 입력순서 정렬
    parsed_files.sort(key=lambda x: (x[0], x[1], x[2]))
    
    # 원본 파일명 순서로 반환
    return [file_info[3] for file_info in parsed_files]
