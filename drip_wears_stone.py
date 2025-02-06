# Dripping Water Wears Stone (滴水穿石) Simulation in Python
# Generated on: 2025-02-06 12:00:00
# Prompt generated on: 2025-02-06 11:59:50
# Signed by ChatGPT

import time

def drip_wears_stone(stone_hardness=100, drip_strength=1, interval=0.05):
    drips = 0
    while stone_hardness > 0:
        stone_hardness -= drip_strength
        drips += 1
        print(f"滴滴... 第 {drips} 次水滴, 剩餘硬度: {max(stone_hardness, 0)}")
        time.sleep(interval)
    print(f"經過 {drips} 次水滴, 石頭終於被穿透!")

if __name__ == '__main__':
    drip_wears_stone()
