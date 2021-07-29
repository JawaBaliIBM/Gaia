from rest_framework import pagination
from rest_framework.response import Response
from multiprocessing import Process

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

import sys, asyncio, logging
sys.path.append("..")

from gaia.serializer import (
    ArticlesSerializer,
    BrandSerializer
)
from gaia.dao.article_dao import ArticleDao
from gaia.dao.brand_dao import BrandDao
from gaia.pagination import CursorPagination

@csrf_exempt
def article_list(request, brand_name, page=None):

    if request.method == 'GET':
        page = request.GET.get('page')
        if not page is None:
            try:
                page = int(page)
                if page < 1:
                    return JsonResponse(
                        {'error_message': 'Param should be positive number'}, status=402)
            except Exception:
                return JsonResponse({'error_message': 'Param should be postive number'}, status=402)

        pagination = CursorPagination(ArticleDao.get_articles_by_brand, url=request.build_absolute_uri())
        pagination.paginate_query(brand_name, page)
        serializer = ArticlesSerializer(pagination.paginate_result())

        return JsonResponse(serializer.data, safe=False, status=200)

@csrf_exempt
def brand_detail(request, name):

    if request.method == 'GET':
        brand = BrandDao.get_brand_by_name(name.lower())
        if brand is None:
            return JsonResponse({'error_message': 'Drand not found'}, status=404)

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
        label_news = Process(target=warning, args=('async task here',))
        label_news.start()

        return JsonResponse({'success': True}, status=200)

def warning(data):
    logging.warning(data)