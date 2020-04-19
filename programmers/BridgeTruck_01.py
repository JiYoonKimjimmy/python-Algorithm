def solution(bridge_length, weight, truck_weights):
    # [프로그래머스 문제 : 다리를 지나는 트럭]
    # - 트럭을 하나씩 꺼내 무게 비교 후 다리 위에 append
    # - queue 에서 하나씩 이동하며 answer 증가
    # - 만약, 무게가 견디지 못한다면 queue 에 0 을 append
    answer = 0

    # bridge queue
    bridge_q = [0] * bridge_length

    while bridge_q:
        answer += 1
        bridge_q.pop(0)

        if truck_weights:
            if sum(bridge_q) + truck_weights[0] <= weight:
                bridge_q.append(truck_weights.pop(0))
            else:
                bridge_q.append(0)

    return answer


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
print("answer : ", solution(bridge_length, weight, truck_weights))