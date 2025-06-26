import time
import heapq

class PrintJob:
    def __init__(self, job_id, priority, arrival_time):
        self.job_id = job_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.last_aged_time = arrival_time

    def age(self, current_time, aging_interval):
        if (current_time - self.last_aged_time) >= aging_interval:
            self.priority -= 1  # Higher priority = lower number
            self.last_aged_time = current_time

    def __lt__(self, other):
        # For priority queue: lower priority value first, then earlier arrival time
        if self.priority == other.priority:
            return self.arrival_time < other.arrival_time
        return self.priority < other.priority

    def __repr__(self):
        return f"Job({self.job_id}, P={self.priority}, T={self.arrival_time})"

class PrintQueueSimulator:
    def __init__(self, aging_interval=5):
        self.jobs = []
        self.time = 0
        self.aging_interval = aging_interval
        self.job_counter = 0

    def add_job(self, priority):
        job = PrintJob(self.job_counter, priority, self.time)
        heapq.heappush(self.jobs, job)
        print(f"[Time {self.time}] Added {job}")
        self.job_counter += 1

    def simulate_time(self, ticks=1):
        for _ in range(ticks):
            self.time += 1
            self._apply_aging()

    def _apply_aging(self):
        # Rebuild heap after aging
        for job in self.jobs:
            job.age(self.time, self.aging_interval)
        heapq.heapify(self.jobs)

    def process_next_job(self):
        if self.jobs:
            job = heapq.heappop(self.jobs)
            print(f"[Time {self.time}] Processing {job}")
        else:
            print(f"[Time {self.time}] No jobs to process.")

    def print_queue(self):
        print(f"[Time {self.time}] Current Queue:")
        for job in sorted(self.jobs):
            print(f" - {job}")

# 🔁 Example Usage
if __name__ == "__main__":
    sim = PrintQueueSimulator(aging_interval=3)
    sim.add_job(priority=5)
    sim.simulate_time(1)
    sim.add_job(priority=4)
    sim.simulate_time(1)
    sim.add_job(priority=5)
    
    sim.print_queue()
    sim.simulate_time(2)  # Trigger aging

    sim.print_queue()
    sim.process_next_job()
    sim.process_next_job()
