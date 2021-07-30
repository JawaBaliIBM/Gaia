from django.urls import path, re_path
from django.conf.urls import url
from gaia.views import (
    brand_detail,
    article_list,
    news_scraper
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
     path('articles/<str:brand_name>/',
         article_list,
         name = 'articles'),
     re_path(r'^articles/<str:brand_name>/$',
         article_list,
         name = 'articles'),
     path('brand/<str:name>/',
         brand_detail,
         name = 'brand'),
     path('news-scraper',
         news_scraper,
         name = 'news-scraper'),
]