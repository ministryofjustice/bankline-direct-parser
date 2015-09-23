class IndexTrackingIterator(object):

    def __init__(self, list):
        self.iterator = iter(list)
        self.current_index = 0

    def __next__(self):
        item = next(self.iterator)
        self.current_index += 1
        return item
