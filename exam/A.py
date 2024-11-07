import sys
from typing import List, Tuple

class Computer:
    def __init__(self, T: int, B: int, Y: int):
        self.T = T
        self.B = B
        self.Y = Y

def check(N: int, computers: List[Computer], max_time: int) -> bool:
    total_processed = 0
    for comp in computers:
        cycle_time = comp.B * comp.T + comp.Y
        full_cycles = max_time // cycle_time
        remaining_time = max_time % cycle_time
        parcels_in_full_cycles = full_cycles * comp.B
        parcels_in_remaining_time = min(comp.B, remaining_time // comp.T)

        total_processed += parcels_in_full_cycles + parcels_in_remaining_time
        if total_processed >= N:
            return True
    return total_processed >= N

def find_min(N: int, computers: List[Computer]) -> Tuple[int, List[int]]:
    lo, hi = 1, sys.maxsize // 2  # Large upper bound
    best_time = hi

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if check(N, computers, mid):
            best_time = mid
            hi = mid - 1
        else:
            lo = mid + 1

    allocation = [0] * len(computers)
    remaining_parcels = N

    for i, comp in enumerate(computers):
        if remaining_parcels <= 0:
            break
        comp_time = best_time
        cycle_time = comp.B * comp.T + comp.Y
        full_cycles = comp_time // cycle_time
        remaining_time = comp_time % cycle_time
        parcels_in_full_cycles = full_cycles * comp.B
        parcels_in_remaining_time = min(comp.B, remaining_time // comp.T)
        total_parcels = min(remaining_parcels, parcels_in_full_cycles + parcels_in_remaining_time)

        allocation[i] = total_parcels
        remaining_parcels -= total_parcels

    return best_time, allocation


n, m = map(int, input().split())
computers = [Computer(*map(int, input().split())) for _ in range(m)]
result = find_min(n, computers)
print(result[0])
print(*result[1])

