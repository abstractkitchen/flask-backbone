import math


class Pagination(object):
    def __init__(self, query, page, per_page, total, items):

        #: The query object that was used to create this pagination object.
        self.query = query

        #: The current page number (1 indexed).
        self.page = page

        #: The number of items to be displayed on a page.
        self.per_page = per_page

        #: The total number of items matching the query.
        self.total = total

        #: The items for the current page.
        self.items = items

        if self.per_page == 0:
            self.pages = 0
        else:
            #: The total number of pages.
            self.pages = int(math.ceil(self.total / float(self.per_page)))

        #: Number of the previous page.
        self.prev_num = self.page - 1

        #: True if a previous page exists.
        self.has_prev = self.page > 1

        #: Number of the next page.
        self.next_num = self.page + 1

        #: True if a next page exists.
        self.has_next = self.page < self.pages

    def prev(self, error_out=False):
        """Returns a `Pagination` object for the previous page."""
        assert self.query is not None, \
            'a query object is required for this method to work'

        return self.query.paginate(self.page - 1, self.per_page, error_out)

    def next(self, error_out=False):
        """Returns a `Pagination` object for the next page."""
        assert self.query is not None, \
            'a query object is required for this method to work'

        return self.query.paginate(self.page + 1, self.per_page, error_out)