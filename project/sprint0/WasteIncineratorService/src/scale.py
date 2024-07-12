import time
import random
import sys

wait_time = sys.argv[1] if len(sys.argv) > 1 else 1

def measure_weight():
    return random.randint(0, 10) * 50

while True:
    print(measure_weight())
    time.sleep(int(wait_time))
