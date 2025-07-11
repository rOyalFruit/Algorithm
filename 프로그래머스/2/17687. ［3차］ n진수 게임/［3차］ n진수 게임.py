def solution(n, t, m, p):
    digits = "0123456789ABCDEF"

    def convert_base(num, base):
        """숫자를 base 진법 문자열로 변환하는 헬퍼 함수"""
        if num == 0:
            return "0"
        
        result = ""
        while num > 0:
            num, remainder = divmod(num, base)
            result = digits[remainder] + result # 나머지에 해당하는 문자를 앞에 추가
        return result

    # 1. 게임에서 말하는 전체 숫자 문자열 생성
    game_string = ""
    num = 0
    required_length = m * t 
    
    while len(game_string) < required_length:
        game_string += convert_base(num, n)
        num += 1

    # 2. 튜브가 말해야 하는 숫자들만 추출
    return game_string[p-1:t*m:m]

