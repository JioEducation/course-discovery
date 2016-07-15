from rest_framework import pagination
from rest_framework.response import Response


class PageNumberPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'


class NamespacedPageNumberPagination(pagination.PageNumberPagination):
    """
    Rjio custom: Pagination scheme that returns results with pagination metadata
    embedded in a "pagination" attribute.  Can be used with data
    that comes as a list of items, or as a dict with a "results"
    attribute that contains a list of items.
    """

    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        """
        Annotate the response with pagination information
        """
        metadata = {
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'num_pages': self.page.paginator.num_pages,
        }
        if isinstance(data, dict):
            if 'results' not in data:
                raise TypeError(u'Malformed result dict')
            data['pagination'] = metadata
        else:
            data = {
                'results': data,
                'pagination': metadata,
            }
        return Response(data)
