class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        fleet = 0 
        max_time = 0.0
        for pos, spd in pairs:
            time = (target - pos)/ spd
            if time > max_time:
                fleet += 1
                max_time = time
        return fleet