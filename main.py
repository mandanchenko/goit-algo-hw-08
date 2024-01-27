import heapq


def minimize_cost(cables):
    heapq.heapify(cables)
    res = []

    while len(cables) > 1:
        min_el1 = heapq.heappop(cables)
        min_el2 = heapq.heappop(cables)
        res.append(min_el1 + min_el2)
        heapq.heappush(cables, min_el1 + min_el2)

    total_cost = sum(heapq.merge(res))
    return total_cost


cables = [1, 2, 4, 10]
total_cost = minimize_cost(cables)
print(total_cost)
