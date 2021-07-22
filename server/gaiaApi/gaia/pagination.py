import os, re, logging

PAGE_PATTERN = '\?page=\d+'

class CursorPagination:
    def __init__(self, query_func, url):
        super().__init__()
        self.__query_func = query_func
        self.__base_url = self.__build_base_url(url)
        self.__next = None
        self.__prev = None
        self.__result = None

    def __build_base_url(self, url):
        return re.sub(re.compile(PAGE_PATTERN), '', url)

    def __build_url_with_page(self, page):
        return '{}?page={}'.format(self.__base_url, page)

    def paginate_query(self, selector: str, page):
        current_page = 1 if page is None else page

        if current_page > 1:
            self.__prev = self.__build_url_with_page(current_page - 1)

        self.__result = self.__query_func(selector, current_page)

        if len(self.__query_func(selector, current_page + 1, 1)) > 0:
            self.__next = self.__build_url_with_page(current_page + 1)

    def paginate_result(self):
        return {
            'results': self.__result,
            'next': self.__next,
            'prev': self.__prev
        }
