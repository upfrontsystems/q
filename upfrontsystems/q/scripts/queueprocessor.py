import sys
import logbook
from logbook import handlers

from pyga.requests import Tracker, Page, Session, Visitor

from redis import Redis
from redis.exceptions import ConnectionError

from rq import Queue, Worker
from rq.scripts.rqworker import format_colors, setup_loghandlers
from rq.scripts import add_standard_arguments
from rq.scripts import setup_redis


class QueueArgs(object):
    """ Can be elaborated to read a config file.
    """
    def __init__(self):
        self.host = 'localhost'
        self.port = 6379
        self.db = 0

        self.burst = False
        self.name = 'GA queue processor'
        self.path = ''
        self.verbose = True
        self.queues = ['google_analytics_q',]


def processqueue():
    args = QueueArgs()
    setup_loghandlers(args)
    setup_redis(args)
    try:
        queues = map(Queue, args.queues)
        w = Worker(queues, name=args.name)
        w.work(burst=args.burst)
    except ConnectionError as e:
        print(e)
        sys.exit(1)


def deliver(entry):
    # make the call to google analytics
    tracker = Tracker(entry['gacode'], entry['domain'])
    visitor = Visitor()
    visitor.ip_address = entry['ip_address'] 
    session = Session()
    # drop the science or maths from the path
    path_elements = ('',) + entry['path'][2:]
    page = Page('/'.join(path_elements))
    tracker.track_pageview(page, session, visitor)
