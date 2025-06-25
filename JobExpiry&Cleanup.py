def remove_expired_jobs(self):

    """
    Track waiting times for all jobs.
    Automatically remove expired jobs after a configured expiry time.
    Notify the system and users when jobs expire.
    """

    expired_jobs = []
    remaining_jobs = []

    for job in self.queue:
        waiting_time = self.current_time - job['submission_time']
        if waiting_time >= self.expiry_limit:
            expired_jobs.append(job)
        else:
            remaining_jobs.append(job)

    # update the queue with only valid jobs
    # ie keep only valid jobs
    self.queue = remaining_jobs

    # notify users of expired jobs
    for job in expired_jobs:
        print(f"[Expired] Job {job['job_id']} from user {job['user_id']} expired after {self.expiry_limit} ticks.")