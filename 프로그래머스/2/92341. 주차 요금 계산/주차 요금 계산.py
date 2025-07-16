import math
from collections import defaultdict


def time_to_minutes(time_str: str) -> int:
    """시간 문자열("HH:MM")을 분으로 변환"""
    hour, minute = map(int, time_str.split(":"))
    return hour * 60 + minute


def calculate_fee(total_minutes: int, fees: list) -> int:
    """누적 주차 시간에 대한 최종 요금 계산"""
    base_time, base_fee, unit_time, unit_fee = fees
    
    if total_minutes <= base_time:
        return base_fee
    
    # 기본 시간을 초과한 경우 추가 요금 계산
    extra_minutes = total_minutes - base_time
    # math.ceil을 사용하여 올림 처리
    additional_fee = math.ceil(extra_minutes / unit_time) * unit_fee
    
    return base_fee + additional_fee


def solution(fees, records):
    # 차량별 누적 주차 시간을 저장하는 딕셔너리
    total_parked_time = defaultdict(int)
    # 현재 주차장에 있는 차량의 입차 시간을 저장하는 딕셔너리
    parking_lot = {}
    
    # 1. 입/출차 기록을 순회하며 누적 시간 계산
    for record in records:
        time, car_number, status = record.split()
        
        if status == "IN":
            parking_lot[car_number] = time
        else: # status == "OUT"
            in_time_str = parking_lot.pop(car_number) # 입차 기록을 가져오고, 주차장에서 제거
            
            parked_duration = time_to_minutes(time) - time_to_minutes(in_time_str)
            total_parked_time[car_number] += parked_duration
            
    # 2. 출차 기록이 없는 차량 처리(23:59에 출차한 것으로 간주)
    end_of_day = "23:59"
    for car_number, in_time_str in parking_lot.items():
        parked_duration = time_to_minutes(end_of_day) - time_to_minutes(in_time_str)
        total_parked_time[car_number] += parked_duration
        
    # 3. 차량 번호 오름차순으로 정렬하여 요금 계산
    result = []
    sorted_car_numbers = sorted(total_parked_time.keys())
    
    for car_number in sorted_car_numbers:
        total_minutes = total_parked_time[car_number]
        fee = calculate_fee(total_minutes, fees)
        result.append(fee)
        
    return result
