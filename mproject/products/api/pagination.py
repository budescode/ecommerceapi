from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
    )


class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10000000000000
    max_limit = 300000000

class PostNumberPagination(PageNumberPagination):
    page_size = 0
