from collections import deque


class HitCounter:
    def __init__(self):
        self.hit_queue = deque()

    def hit(self, timestamp: int):
        self.hit_queue.appendleft(timestamp)

    def get_hits(self, timestamp):
        while True:
            if len(self.hit_queue) == 0:
                return 0
            latest_timestamp = self.hit_queue.pop()
            if timestamp - latest_timestamp < 300:
                self.hit_queue.append(latest_timestamp)
                return len(self.hit_queue)


if __name__ == '__main__':
    counter = HitCounter()
    counter.hit(1)
    counter.hit(2)
    counter.hit(3)
    print(counter.get_hits(4))
    counter.hit(300)
    print(counter.get_hits(300))
    # counter.hit(301)
    print(counter.get_hits(301))