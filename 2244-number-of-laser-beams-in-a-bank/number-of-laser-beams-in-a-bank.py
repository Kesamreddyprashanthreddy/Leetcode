class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        devices_per_row = [row.count('1') for row in bank if row.count('1') > 0]
        
        total_beams = 0
        for i in range(1, len(devices_per_row)):
            total_beams += devices_per_row[i - 1] * devices_per_row[i]
        
        return total_beams