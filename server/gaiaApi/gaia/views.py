from rest_framework import pagination
from rest_framework.response import Response
from multiprocessing import Process

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from rest_framework.parsers import JSONParser

import asyncio, logging

from gaia.serializer import (
    ArticlesSerializer,
    BrandSerializer,
    ArticlesWithIndexSerializer
)
from gaia.jobs.analyze import analyze
from gaia.dao.article_dao import ArticleDao
from gaia.dao.brand_dao import BrandDao
from gaia.pagination import CursorPagination
from gaia.gaia_utils import GaiaUtils

INDEX_URL_FORMAT = '{base_url}/?page={page}&page_size={page_size}'

@csrf_exempt
def article_list(request, brand_name):
    brand_name = brand_name.lower()
    def handle_request_with_page_size(page, page_size):
        base_url = request.build_absolute_uri('/articles/{}'.format(brand_name))

        try:
            page = GaiaUtils.convert_positive_int(page)
            page_size = GaiaUtils.convert_positive_int(page_size)
        except Exception:
            return JsonResponse(
                        {'error_message': 'Param should be positive number'.format(page, page_size)}, status=402)

        articles = ArticleDao.get_articles_by_brand(brand_name)
        paginator = Paginator(articles, page_size)
        current_page = paginator.page(page)
        next = None
        prev = None

        if current_page.has_next():
            next = INDEX_URL_FORMAT.format(
                base_url=base_url, 
                page=page+1, 
                page_size=page_size
            )

        if current_page.has_previous():
            prev = INDEX_URL_FORMAT.format(
                base_url=base_url, 
                page=page-1, 
                page_size=page_size
            )

        result = {
            'total': paginator.count,
            'next': next,
            'prev': prev,
            'results': paginator.page(page).object_list
        }
        serializer = ArticlesWithIndexSerializer(result)

        return JsonResponse(serializer.data, safe=False, status=200)

    def handle_request(page):
        if not page is None:
            try:
                page = GaiaUtils.convert_positive_int(page)
            except Exception:
                return JsonResponse(
                            {'error_message': 'Param should be positive number'}, status=402)

        pagination = CursorPagination(ArticleDao.get_articles_by_brand_with_limit, 
            url=request.build_absolute_uri())
        pagination.paginate_query(brand_name, page)
        serializer = ArticlesSerializer(pagination.paginate_result())

        return JsonResponse(serializer.data, safe=False, status=200)

    if request.method == 'GET':
        page = request.GET.get('page')
        page_size = request.GET.get('page_size')

        if not page_size is None:
            return handle_request_with_page_size(page, page_size)

        return handle_request(page)

@csrf_exempt
def brand_detail(request, name):

    if request.method == 'GET':
        brand = BrandDao.get_brand_by_name(name.lower())
        if brand is None:
            return JsonResponse({'error_message': 'Brand not found'}, status=404)

        serializer = BrandSerializer(brand)
        return JsonResponse(serializer.data, safe=False, status=200)

@csrf_exempt
def news_scraper(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)

        '''
            TODO: change to label news task
            data = {
                'filename': filename,
                'bucket_name': bucket_name
            }
        '''
        label_news = Process(target=analyze, args=(data["filename"],))
        label_news.start()

        return JsonResponse({'success': True}, status=200)

def warning(data):
    logging.warning(data)