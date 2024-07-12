import time
import random
import sys

wait_time = sys.argv[1] if len(sys.argv) > 1 else 1

def get_distance():
    return random.randint(0, 2000)

while True:
    print(get_distance())
    time.sleep(int(wait_time))
