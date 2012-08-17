from redis import Redis
from rq import Queue


def get_q(q_name):
    q = Queue(connection=Redis())
    q.enqueue(deliver, entry)
