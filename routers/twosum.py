from fastapi import APIRouter

router = APIRouter()

@router.get("/two-sum")
def solve_twosum(nums: str, target: int):
    arr = list(map(int, nums.split(",")))
    lookup = {}
    
    for i, n in enumerate(arr):
        diff = target - n
        if diff in lookup:
            return {"indices": [lookup[diff], i]}
        lookup[n] = i
    
    return {"message": "No solution"}