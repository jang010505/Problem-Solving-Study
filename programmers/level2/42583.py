from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0

    dq = deque()

    for i in range(bridge_length):
        dq.append(0)

    bridge_weights = 0

    while dq:
        answer += 1
        bridge_weights -= dq.popleft()


        if truck_weights:
            if bridge_weights + truck_weights[0] > weight:
                dq.append(0)
            else:
                bridge_weights += truck_weights[0]
                dq.append(truck_weights.pop(0))

    return answer