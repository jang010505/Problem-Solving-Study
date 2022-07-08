import heapq

def solution(operations):
    answer = []
    heap = []

    for data in operations:
        op = data.split()

        if op[0] == "I":
            heapq.heappush(heap, int(op[1]))
        elif op[0] == "D":
            if not heap:
                continue
            elif int(op[1]) < 0:
                heapq.heappop(heap)
            else:
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
    if heap:
        answer = [max(heap), min(heap)]
    else:
        answer = [0, 0]
    return answer