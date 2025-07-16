import math
from collections import defaultdict


def func(in_time, out_time):
    in_hour, in_minute = map(int, in_time.split(":"))
    out_hour, out_minute = map(int, out_time.split(":"))
    
    in_total = in_hour * 60 + in_minute
    out_total = out_hour * 60 + out_minute
    
    return out_total - in_total
        

def func2(times, fees):
    result = []
    a, b, c, d = fees
    lst = [v for k, v in sorted(times.items())]

    for time in lst:
        if time <= a:
            result.append(b)
            continue
        result.append(b + math.ceil((time - a) / c) * d)
        
    return result


def solution(fees, records):
    d = dict()
    total_time = defaultdict(int)
    
    for record in records:
        time, car_num, io = record.split(" ")
        if io == "IN":
            d[car_num] = time
        else:
            in_time = d[car_num]
            total_time[car_num] += func(in_time, time)
            del d[car_num]
        
    for car_num in list(d.keys()):
        in_time = d[car_num]
        total_time[car_num] += func(in_time, "23:59")
        del d[car_num]
    
    return func2(total_time, fees)