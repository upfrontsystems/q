from pyga.requests import Tracker, Page, Session, Visitor

def processqueue():
    import pdb;pdb.set_trace()
    return

def deliver():
    # make the call to google analytics
    tracker = Tracker(gacode, domain)
    visitor = Visitor()
    visitor.ip_address = self.request.getClientAddr()
    session = Session()
    # drop the science or maths from the path
    path_elements = ('',) + self.context.getPhysicalPath()[2:]
    page = Page('/'.join(path_elements))
    tracker.track_pageview(page, session, visitor)
