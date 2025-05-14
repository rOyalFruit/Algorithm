def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length
    current_weight = 0
    
    while len(truck_weights) > 0:
        time += 1
        current_weight -= bridge.pop(0)
        
        if current_weight + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            bridge.append(truck)
            current_weight += truck
        else:
            bridge.append(0)
            
    return bridge_length + time